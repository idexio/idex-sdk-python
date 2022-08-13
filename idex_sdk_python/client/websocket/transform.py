from typing import Callable, Dict, Union, cast

from idex_sdk_python.idex_types.websocket.request import (
    WebSocketRequestSubscribeShortNames,
)
from idex_sdk_python.idex_types.websocket.response import (
    WebSocketResponse,
    WebSocketResponseBalanceLong,
    WebSocketResponseBalanceShort,
    WebSocketResponseCandleLong,
    WebSocketResponseCandleShort,
    WebSocketResponseError,
    WebSocketResponseL1OrderBookLong,
    WebSocketResponseL1OrderBookShort,
    WebSocketResponseL2OrderBookLong,
    WebSocketResponseL2OrderBookShort,
    WebSocketResponseOrderFillLong,
    WebSocketResponseOrderFillShort,
    WebSocketResponseOrderLong,
    WebSocketResponseOrderShort,
    WebSocketResponseSubscriptionMessageLong,
    WebSocketResponseSubscriptionMessageShort,
    WebSocketResponseSubscriptions,
    WebSocketResponseTickerLong,
    WebSocketResponseTickerShort,
    WebSocketResponseTokenPriceLong,
    WebSocketResponseTokenPriceShort,
    WebSocketResponseTradeLong,
    WebSocketResponseTradeShort,
)


def transform_tickers_mesg(ticker: WebSocketResponseTickerShort) -> WebSocketResponseTickerLong:
    return {
        "market": ticker["m"],
        "time": ticker["t"],
        "open": ticker["o"],
        "high": ticker["h"],
        "low": ticker["l"],
        "close": ticker["c"],
        "closeQuantity": ticker["Q"],
        "baseVolume": ticker["v"],
        "quoteVolume": ticker["q"],
        "percentChange": ticker["P"],
        "numTrades": ticker["n"],
        "ask": ticker["a"],
        "bid": ticker["b"],
        "sequence": ticker["u"],
    }


def transform_trades_mesg(mesg: WebSocketResponseTradeShort) -> WebSocketResponseTradeLong:
    return {
        "type": mesg["y"],
        "market": mesg["m"],
        "fillId": mesg["i"],
        "price": mesg["p"],
        "quantity": mesg["q"],
        "quoteQuantity": mesg["Q"],
        "time": mesg["t"],
        "makerSide": mesg["s"],
        "sequence": mesg["u"],
    }


def transform_candles_mesg(candle: WebSocketResponseCandleShort) -> WebSocketResponseCandleLong:
    return {
        "market": candle["m"],
        "time": candle["t"],
        "interval": candle["i"],
        "start": candle["s"],
        "end": candle["e"],
        "open": candle["o"],
        "high": candle["h"],
        "low": candle["l"],
        "close": candle["c"],
        "volume": candle["v"],
        "numTrades": candle["n"],
        "sequence": candle["u"],
    }


def transform_l1orderbook_mesg(
    l1orderbook: WebSocketResponseL1OrderBookShort,
) -> WebSocketResponseL1OrderBookLong:
    return {
        "market": l1orderbook["m"],
        "time": l1orderbook["t"],
        "bidPrice": l1orderbook["b"],
        "bidQuantity": l1orderbook["B"],
        "askPrice": l1orderbook["a"],
        "askQuantity": l1orderbook["A"],
        "pool": (
            None
            if not l1orderbook["p"]
            else {
                "baseReserveQuantity": l1orderbook["p"]["q"],
                "quoteReserveQuantity": l1orderbook["p"]["Q"],
            }
        ),
    }


def transform_l2orderbook_mesg(
    l2orderbook: WebSocketResponseL2OrderBookShort,
) -> WebSocketResponseL2OrderBookLong:
    return {
        "market": l2orderbook["m"],
        "time": l2orderbook["t"],
        "sequence": l2orderbook["u"],
        "bids": l2orderbook["b"],
        "asks": l2orderbook["a"],
        "pool": (
            None
            if not l2orderbook["p"]
            else {
                "baseReserveQuantity": l2orderbook["p"]["q"],
                "quoteReserveQuantity": l2orderbook["p"]["Q"],
            }
        ),
    }


def transform_balances_mesg(balance: WebSocketResponseBalanceShort) -> WebSocketResponseBalanceLong:
    return {
        "wallet": balance["w"],
        "asset": balance["a"],
        "quantity": balance["q"],
        "availableForTrade": balance["f"],
        "locked": balance["l"],
        "usdValue": balance["d"],
    }


def transform_order_fill(
    fill: WebSocketResponseOrderFillShort,
) -> WebSocketResponseOrderFillLong:
    return {
        "type": fill["y"],
        "fillId": fill["i"],
        "price": fill["p"],
        "quantity": fill["q"],
        "quoteQuantity": fill["Q"],
        "orderBookQuantity": fill["oq"],
        "orderBookQuoteQuantity": fill["oQ"],
        "poolQuantity": fill["pq"],
        "poolQuoteQuantity": fill["pQ"],
        "time": fill["t"],
        "makerSide": fill["s"],
        "sequence": fill["u"],
        "fee": fill["f"],
        "feeAsset": fill["a"],
        "gas": fill["g"],
        "liquidity": fill["l"],
        "txId": fill["T"],
        "txStatus": fill["S"],
    }


def transform_orders_mesg(order: WebSocketResponseOrderShort) -> WebSocketResponseOrderLong:
    return {
        "market": order["m"],
        "orderId": order["i"],
        "clientOrderId": order["c"],
        "wallet": order["w"],
        "executionTime": order["t"],
        "time": order["T"],
        "update": order["x"],
        "status": order["X"],
        "sequence": order["u"],
        "type": order["o"],
        "side": order["S"],
        "originalQuantity": order["q"],
        "originalQuoteQuantity": order["Q"],
        "executedQuantity": order["z"],
        "cumulativeQuoteQuantity": order["Z"],
        "avgExecutionPrice": order["v"],
        "price": order["p"],
        "stopPrice": order["P"],
        "timeInForce": order["f"],
        "selfTradePrevention": order["V"],
        "fills": list(map(transform_order_fill, order["F"])),
    }


def transform_tokenprice_mesg(
    tokenprice: WebSocketResponseTokenPriceShort,
) -> WebSocketResponseTokenPriceLong:
    return {
        "token": tokenprice["t"],
        "price": tokenprice["p"],
    }


MESG_DATA_TRANSFORM_FUNCS: Dict[WebSocketRequestSubscribeShortNames, Callable] = {
    "tickers": transform_tickers_mesg,
    "candles": transform_candles_mesg,
    "trades": transform_trades_mesg,
    "l1orderbook": transform_l1orderbook_mesg,
    "l2orderbook": transform_l2orderbook_mesg,
    "balances": transform_balances_mesg,
    "orders": transform_orders_mesg,
    "tokenprice": transform_tokenprice_mesg,
}


def transform_websocket_short_response_mesg(
    mesg: Union[
        WebSocketResponseError,
        WebSocketResponseSubscriptions,
        WebSocketResponseSubscriptionMessageShort,
    ]
) -> WebSocketResponse:
    if mesg["type"] in ("error", "subscriptions"):
        return cast(Union[WebSocketResponseError, WebSocketResponseSubscriptions], mesg)
    mesg = cast(WebSocketResponseSubscriptionMessageShort, mesg)

    transform = MESG_DATA_TRANSFORM_FUNCS.get(mesg["type"])
    if not transform:
        return cast(WebSocketResponse, mesg)

    long_mesg = {
        "type": mesg["type"],
        "data": transform(mesg["data"]),
    }
    return cast(WebSocketResponseSubscriptionMessageLong, long_mesg)
