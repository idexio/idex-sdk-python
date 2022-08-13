from typing import Any, Dict, List, Optional

import requests

from idex_sdk_python.client.utils import derive_base_url
from idex_sdk_python.constants import REST_API_KEY_HEADER
from idex_sdk_python.idex_types.enums import MultiverseChain
from idex_sdk_python.idex_types.errors import check_response_errors
from idex_sdk_python.idex_types.rest.request import (
    RestRequestFindCandles,
    RestRequestFindLiquidityPools,
    RestRequestFindMarkets,
    RestRequestFindTrades,
)
from idex_sdk_python.idex_types.rest.response import (
    RestResponseAsset,
    RestResponseCandle,
    RestResponseExchangeInfo,
    RestResponseLiquidityPool,
    RestResponseMarket,
    RestResponseOrderBook,
    RestResponseTicker,
    RestResponseTrade,
)


class RestPublicClient:
    base_url: str
    multiverse_chain: MultiverseChain
    sandbox: bool
    session: requests.Session

    def __init__(
        self,
        multiverse_chain: MultiverseChain = MultiverseChain.MATIC,
        sandbox: bool = False,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> None:
        self.base_url = derive_base_url(
            api_type="rest",
            multiverse_chain=multiverse_chain,
            sandbox=sandbox,
            override_base_url=base_url,
        )
        self.multiverse_chain = multiverse_chain
        self.sandbox = sandbox
        self.session = requests.Session()
        if api_key:
            self.session.headers[REST_API_KEY_HEADER] = api_key

    def _get(self, endpoint: str, params: Any = None) -> Any:
        res = self.session.get(self.base_url + endpoint, params=params)
        check_response_errors(res)
        return res.json()

    # Public Data Endpoints

    def ping(self) -> Dict:
        """
        Test connectivity to the REST API
        See https://api-docs-v3.idex.io/#get-ping
        """
        return self._get("/ping")

    def get_server_time(self) -> int:
        """
        Returns the current server time
        See https://api-docs-v3.idex.io/#get-time
        """
        res = self._get("/time")
        return res["serverTime"]

    def get_exchange_info(self) -> RestResponseExchangeInfo:
        """
        Returns basic information about the exchange
        See https://api-docs-v3.idex.io/#get-exchange
        """
        return self._get("/exchange")

    def get_assets(self) -> List[RestResponseAsset]:
        """
        Returns information about assets supported by the exchange
        See https://api-docs-v3.idex.io/#get-assets
        """
        return self._get("/assets")

    def get_markets(
        self, find_markets: Optional[RestRequestFindMarkets] = None
    ) -> List[RestResponseMarket]:
        """
        Returns information about the currently listed markets
        See https://api-docs-v3.idex.io/#get-markets
        """
        return self._get("/markets", find_markets)

    def get_liquidity_pools(
        self, find_liquidity_pools: Optional[RestRequestFindLiquidityPools] = None
    ) -> List[RestResponseLiquidityPool]:
        """
        Returns information about liquidity pools supported by the exchange
        See https://api-docs-v3.idex.io/#get-liquidity-pools
        """
        return self._get("/liquidityPools", find_liquidity_pools)

    # Market Data Endpoints

    def get_tickers(self, market: Optional[str] = None) -> List[RestResponseTicker]:
        """
        Returns market statistics for the trailing 24-hour period
        """
        return self._get("/tickers", {"market": market})

    def get_candles(self, find_candles: RestRequestFindCandles) -> List[RestResponseCandle]:
        """
        Returns candle (OHLCV) data for a market
        See https://api-docs-v3.idex.io/#get-candles
        """
        return self._get("/candles", find_candles)

    def get_trades(self, find_trades: RestRequestFindTrades) -> List[RestResponseTrade]:
        """
        Returns public trade data for a market
        See https://api-docs-v3.idex.io/#get-trades
        """
        return self._get("/trades", find_trades)

    def get_order_book_level1(
        self, market: str, limit_order_only: bool = False
    ) -> List[RestResponseOrderBook]:
        """
        Get current top bid/ask price levels of order book for a market
        See https://api-docs-v3.idex.io/#get-order-books
        """
        return self._get(
            "/orderbook", {"level": 1, "limitOrderOnly": limit_order_only, "market": market}
        )

    def get_order_book_level2(
        self, market: str, limit: int = 50, limit_order_only: bool = False
    ) -> RestResponseOrderBook:
        """
        Get current order book price levels for a market
        See https://api-docs-v3.idex.io/#get-order-books
        """
        return self._get(
            "/orderbook",
            {"level": 2, "limit": limit, "limitOrderOnly": limit_order_only, "market": market},
        )
