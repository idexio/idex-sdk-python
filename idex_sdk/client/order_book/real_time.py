import asyncio
from typing import Dict, List, Optional, Set, cast

from pyee.asyncio import AsyncIOEventEmitter

from idex_sdk.client.order_book.utils import l1_equal, update_l2_levels
from idex_sdk.client.rest.public import RestPublicClient
from idex_sdk.client.utils import derive_base_url
from idex_sdk.client.websocket.client import WebSocketClient
from idex_sdk.constants import (
    ORDER_BOOK_FIRST_LEVEL_MULTIPLIER_IN_PIPS,
    ORDER_BOOK_HYBRID_SLIPPAGE,
    ORDER_BOOK_MAX_L2_LEVELS,
)
from idex_sdk.idex_types.enums import MultiverseChain
from idex_sdk.idex_types.order_book import (
    L1AndL2OrderBook,
    L1OrderBook,
    L2OrderBook,
    OrderBookFeesAndMinimums,
)
from idex_sdk.idex_types.rest.response import RestResponseOrderBook
from idex_sdk.idex_types.websocket.request import (
    WebSocketRequestL2OrderBookSubscription,
    WebSocketRequestTokenPriceSubscription,
)
from idex_sdk.idex_types.websocket.response import (
    WebSocketResponse,
    WebSocketResponseTokenPriceLong,
)
from idex_sdk.order_book.api_conversions import (
    l1_order_book_to_rest_response,
    l2_order_book_to_rest_response,
    response_to_l2_order_book,
)
from idex_sdk.order_book.hybrid import l2_limit_order_book_to_hybrid_order_books
from idex_sdk.order_book.quantities import aggregate_l2_order_book_at_tick_size
from idex_sdk.order_book.utils import l2_to_l1_order_book
from idex_sdk.pipmath import (
    EXCHANGE_DECIMALS,
    ONE_IN_PIPS,
    decimal_to_pip,
    multiply_pips,
    pip_to_decimal,
)


class OrderBookRealTimeClient(AsyncIOEventEmitter):
    rest_public_client: RestPublicClient
    websocket_client: WebSocketClient
    fees_and_minimums_loaded = False
    taker_idex_fee_rate = 0
    taker_liquidity_provider_fee_rate = 0
    taker_trade_minimum = 0
    l1_order_books: Dict[str, L1OrderBook] = {}
    l2_order_books: Dict[str, L2OrderBook] = {}
    l2_order_book_updates: Dict[str, List[L2OrderBook]] = {}
    markets: List[str] = []
    markets_by_asset_symbol: Dict[str, Set[str]] = {}
    token_prices: Dict[str, Optional[int]] = {}
    is_tick_sizes_loaded: bool = False
    tick_sizes_by_market: Dict[str, int] = {}
    websocket_connection_listeners_configured = False
    websocket_response_listener_configured = False

    def __init__(
        self,
        api_key: Optional[str] = None,
        connect_timeout: Optional[int] = None,
        sandbox: bool = False,
        multiverse_chain: MultiverseChain = MultiverseChain.MATIC,
        rest_base_url: Optional[str] = None,
        websocket_base_url: Optional[str] = None,
        fees_and_minimums_override: Optional[OrderBookFeesAndMinimums] = None,
    ) -> None:
        super().__init__()
        rest_api_url = derive_base_url("rest", multiverse_chain, sandbox, rest_base_url)
        websocket_api_url = derive_base_url(
            "websocket", multiverse_chain, sandbox, websocket_base_url
        )

        self.rest_public_client = RestPublicClient(
            api_key=api_key,
            multiverse_chain=multiverse_chain,
            sandbox=sandbox,
            base_url=rest_api_url,
        )
        self.websocket_client = WebSocketClient(
            api_key=api_key,
            should_reconnect_automatically=True,
            connect_timeout=connect_timeout,
            sandbox=sandbox,
            multiverse_chain=multiverse_chain,
            base_url=websocket_api_url,
        )

        if fees_and_minimums_override:
            self.set_fees_and_minimums_override(fees_and_minimums_override)
            self.fees_and_minimums_loaded = True

    async def start(self, markets: List[str]) -> None:
        """
        Loads initial state from REST API and begin listening to orderbook updates.
        """
        self.markets = markets
        self.map_tokens_to_markets()
        self.setup_internal_websocket()
        await self.websocket_client.connect()

    async def stop(self) -> None:
        """
        Stop the order book client, and reset internal state. Call this when you are no longer
        using the client, to release memory and network resources.
        """
        if self.websocket_client.is_connected():
            await self.unsubscribe()
            await self.websocket_client.disconnect()
        self.reset_internal_state()

    def set_fees_and_minimums_override(self, override: OrderBookFeesAndMinimums) -> None:
        """
        Set custom fee rates for synthetic price level calculations. Use this if your wallet has
        custom fees set.
        """
        self.taker_idex_fee_rate = decimal_to_pip(override["taker_idex_fee_rate"])
        self.taker_liquidity_provider_fee_rate = decimal_to_pip(
            override["taker_liquidity_provider_fee_rate"]
        )
        self.taker_trade_minimum = multiply_pips(
            ORDER_BOOK_FIRST_LEVEL_MULTIPLIER_IN_PIPS,
            decimal_to_pip(override["taker_trade_minimum"]),
        )

    def get_current_fees_and_minimums(self) -> OrderBookFeesAndMinimums:
        return {
            "taker_idex_fee_rate": pip_to_decimal(self.taker_idex_fee_rate),
            "taker_liquidity_provider_fee_rate": pip_to_decimal(
                self.taker_liquidity_provider_fee_rate
            ),
            "taker_trade_minimum": pip_to_decimal(self.taker_trade_minimum),
        }

    def get_maximum_tick_size_under_spread(self, market: str) -> int:
        bids = self.get_order_book_l2(market, 1000)["bids"]
        min_bid_price: Optional[str] = None if len(bids) == 0 else bids[-1][0]
        num_digits = len(str(decimal_to_pip(min_bid_price))) if min_bid_price else EXCHANGE_DECIMALS
        return 10 ** (min(num_digits, EXCHANGE_DECIMALS) - 1)

    def get_order_book_l1(
        self, market: str, tick_size: Optional[int] = None
    ) -> RestResponseOrderBook:
        """
        Load the current state of the level 1 orderbook for this market.

        Args:
            market
            tick_size: minimum price movement expressed in pips (10^-8), defaults to market setting
        """
        return l1_order_book_to_rest_response(self.get_hybrid_books(market, tick_size)["l1"])

    def get_order_book_l2(
        self, market: str, limit: int = 100, tick_size: Optional[int] = None
    ) -> RestResponseOrderBook:
        """
        Load the current state of the level 2 orderbook for this market.

        Args:
            market
            limit: Total number of price levels (bids + asks) to return, between 2 and 1000
            tickSize: minimum price movement expressed in pips (10^-8)
        """
        return l2_order_book_to_rest_response(self.get_hybrid_books(market, tick_size)["l2"], limit)

    def get_hybrid_books(self, market: str, tick_size: Optional[int] = None) -> L1AndL2OrderBook:
        applied_tick_size = tick_size or self.tick_sizes_by_market[market] or 1
        input_book = self.load_level2(market)
        aggregated_l2_book = aggregate_l2_order_book_at_tick_size(input_book, applied_tick_size)
        return l2_limit_order_book_to_hybrid_order_books(
            aggregated_l2_book,
            self.taker_idex_fee_rate,
            self.taker_liquidity_provider_fee_rate,
            True,
            self.get_market_minimum(market),
            applied_tick_size,
            ORDER_BOOK_MAX_L2_LEVELS,
            ORDER_BOOK_HYBRID_SLIPPAGE,
        )

    async def apply_order_book_updates(self, market: str) -> None:
        updates = self.l2_order_book_updates.get(market)
        if not updates:
            return

        book = self.l2_order_books.get(market)
        # If this market has not yet been synchronized from the REST API, then halt processing,
        # messages for the market will queue and process after it runs
        if not book:
            return

        before_l1 = l2_to_l1_order_book(book)
        for update in updates:
            if book["sequence"] > update["sequence"]:
                # outdated sequence, ignore
                continue
            elif book["sequence"] + 1 == update["sequence"]:
                # an expected next update has arrived
                update_l2_levels(book, update)
            elif book["sequence"] == update["sequence"]:
                # the pool was updated (sequence does not increment)
                book["pool"] = update["pool"]
            else:
                # If an invalid update arrives, reset all data and synchronize anew
                self.emit("disconnected")
                self.emit(
                    "error",
                    Exception(
                        f"Missing l2 update sequence, current book is {book['sequence']} "
                        f"message was {update['sequence']}"
                    ),
                )
                await self.unsubscribe()
                self.reset_internal_state()
                await self.subscribe()
                await self.synchronize_from_rest_api()
                self.emit("connected")
                return
        after_l1 = l2_to_l1_order_book(book)

        self.l1_order_books[market] = l2_to_l1_order_book(book)
        if not l1_equal(before_l1, after_l1):
            self.emit("l1", market)
        self.emit("l2", market)
        del self.l2_order_book_updates[market]

    def apply_token_price_update(self, message: WebSocketResponseTokenPriceLong) -> None:
        self.token_prices[message["token"]] = (
            decimal_to_pip(message["price"]) if message["price"] else None
        )
        markets = self.markets_by_asset_symbol.get(message["token"])
        if markets:
            for market in markets:
                self.emit("l1", market)
                self.emit("l2", market)

    async def load_fees_and_minimums(self) -> None:
        # Global fee rates only need to be loaded once as they are static
        # and to allow for overriding
        if self.fees_and_minimums_loaded:
            return

        exchange_info = self.rest_public_client.get_exchange_info()
        self.taker_liquidity_provider_fee_rate = decimal_to_pip(
            exchange_info["takerLiquidityProviderFeeRate"]
        )
        self.taker_idex_fee_rate = decimal_to_pip(exchange_info["takerIdexFeeRate"])
        self.taker_trade_minimum = multiply_pips(
            ORDER_BOOK_FIRST_LEVEL_MULTIPLIER_IN_PIPS,
            decimal_to_pip(exchange_info["takerTradeMinimum"]),
        )
        self.fees_and_minimums_loaded = True

    async def synchronize_from_rest_api(self) -> None:
        async def load_market(market: str) -> None:
            self.l2_order_books[market] = self.load_level2(market)
            self.emit("ready", market)

        # Updates cannot be applied until successfully synchronized with the REST API, so keep
        # trying with exponential backoff until success
        reconnect_attempt = 0
        while True:
            backoff_seconds = 2**reconnect_attempt
            reconnect_attempt += 1
            try:
                # Load minimums and token prices first so synthetic orderbook
                # calculations are accurate
                await asyncio.gather(
                    self.load_fees_and_minimums(), self.load_token_prices(), self.load_tick_sizes()
                )
                await asyncio.gather(*[load_market(market) for market in self.markets])
                return
            except Exception as error:
                self.emit("error", error)
                await asyncio.sleep(backoff_seconds)

    def load_level2(self, market: str) -> L2OrderBook:
        if self.l2_order_books.get(market):
            return self.l2_order_books[market]
        book = self.rest_public_client.get_order_book_level2(market, 1000, True)
        return response_to_l2_order_book(book)

    async def load_token_prices(self) -> None:
        assets = self.rest_public_client.get_assets()
        for asset in assets:
            if asset["symbol"] not in self.token_prices:
                self.token_prices[asset["symbol"]] = (
                    None
                    if not asset.get("maticPrice")
                    else decimal_to_pip(cast(str, asset.get("maticPrice")))
                )

    async def load_tick_sizes(self) -> None:
        # Market tick sizes only need to be loaded once as they are effectively static
        if self.is_tick_sizes_loaded:
            return
        markets = self.rest_public_client.get_markets()
        for market in markets:
            self.tick_sizes_by_market[market["market"]] = decimal_to_pip(market["tickSize"])
        self.is_tick_sizes_loaded = True

    def map_tokens_to_markets(self) -> None:
        for market in self.markets:
            base_symbol, quote_symbol = market.split("-")

            markets_by_base: Set = self.markets_by_asset_symbol.get(base_symbol) or set()
            markets_by_base.add(market)
            self.markets_by_asset_symbol[base_symbol] = markets_by_base

            markets_by_quote: Set = self.markets_by_asset_symbol.get(quote_symbol) or set()
            markets_by_quote.add(market)
            self.markets_by_asset_symbol[quote_symbol] = markets_by_quote

    def get_market_minimum(self, market: str) -> Optional[int]:
        quote_symbol = market.split("-")[1]
        price = self.token_prices.get(quote_symbol)
        return int(self.taker_trade_minimum * ONE_IN_PIPS / price) if price else None

    def reset_internal_state(self) -> None:
        self.taker_idex_fee_rate = 0
        self.taker_liquidity_provider_fee_rate = 0
        self.taker_trade_minimum = 0
        self.token_prices.clear()
        self.l1_order_books.clear()
        self.l2_order_books.clear()
        self.l2_order_book_updates.clear()

    # Connection management

    def setup_internal_websocket(self) -> None:
        if not self.websocket_connection_listeners_configured:
            self.websocket_client.on_connect(self.websocket_handle_connect)
            self.websocket_client.on_disconnect(self.websocket_handle_disconnect)
            self.websocket_client.on_error(self.websocket_handle_error)
            self.websocket_connection_listeners_configured = True

    async def subscribe(self) -> None:
        l2orderbook_mesg: WebSocketRequestL2OrderBookSubscription = {
            "name": "l2orderbook",
            "markets": self.markets,
        }
        tokenprice_mesg: WebSocketRequestTokenPriceSubscription = {
            "name": "tokenprice",
            "markets": self.markets,
        }
        await asyncio.gather(
            self.websocket_client.subscribe([l2orderbook_mesg]),
            self.websocket_client.subscribe([tokenprice_mesg]),
        )

    async def unsubscribe(self) -> None:
        await self.websocket_client.unsubscribe(["l2orderbook", "tokenprice"])

    # Event handlers

    async def websocket_handle_connect(self) -> None:
        if not self.websocket_response_listener_configured:
            self.websocket_client.on_response(self.websocket_handle_response)
            self.websocket_response_listener_configured = True

        await self.subscribe()
        await self.synchronize_from_rest_api()
        self.emit("connected")

    async def websocket_handle_disconnect(self, code: int, reason: str) -> None:
        # Assume messages will be lost during disconnection and clear state.
        # State will be re-synchronized again on reconnect
        self.reset_internal_state()
        self.emit("disconnected")

    async def websocket_handle_error(self, error: Exception) -> None:
        self.emit("error", error)

    async def websocket_handle_response(self, response: WebSocketResponse) -> None:
        if response["type"] == "l2orderbook":
            # accumulate L2 updates to be applied
            updates_to_apply = self.l2_order_book_updates.get(response["data"]["market"], [])
            updates_to_apply.append(response_to_l2_order_book(response["data"]))
            self.l2_order_book_updates[response["data"]["market"]] = updates_to_apply
            await self.apply_order_book_updates(response["data"]["market"])
        if response["type"] == "tokenprice":
            self.apply_token_price_update(response["data"])
