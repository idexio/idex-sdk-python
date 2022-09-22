import math
from typing import List, Optional, Union, cast

from idex_sdk.idex_types.order_book import (
    L1OrderBook,
    L2OrderBook,
    OrderBookLevelL1,
    OrderBookLevelL2,
    PoolReserveQuantities,
)
from idex_sdk.idex_types.rest.response import (
    RestResponseLiquidityPoolReserves,
    RestResponseOrderBook,
    RestResponseOrderBookPriceLevel,
)
from idex_sdk.idex_types.websocket.response import (
    WebSocketResponseL2OrderBookLong,
)
from idex_sdk.pipmath import decimal_to_pip, pip_to_decimal


def l1_order_book_to_rest_response(l1: L1OrderBook) -> RestResponseOrderBook:
    asks: List[RestResponseOrderBookPriceLevel] = [
        (
            pip_to_decimal(l1["asks"]["price"]),
            pip_to_decimal(l1["asks"]["size"]),
            l1["asks"]["num_orders"],
        )
    ]
    bids: List[RestResponseOrderBookPriceLevel] = [
        (
            pip_to_decimal(l1["bids"]["price"]),
            pip_to_decimal(l1["bids"]["size"]),
            l1["bids"]["num_orders"],
        )
    ]
    return {
        "sequence": l1["sequence"],
        "asks": asks,
        "bids": bids,
        "pool": None
        if not l1["pool"]
        else {
            "baseReserveQuantity": pip_to_decimal(l1["pool"]["base_reserve_quantity"]),
            "quoteReserveQuantity": pip_to_decimal(l1["pool"]["quote_reserve_quantity"]),
        },
    }


def order_book_level_to_response_level(
    order_book_level: Union[OrderBookLevelL1, OrderBookLevelL2],
) -> RestResponseOrderBookPriceLevel:
    level: RestResponseOrderBookPriceLevel = (
        pip_to_decimal(order_book_level["price"]),
        pip_to_decimal(order_book_level["size"]),
        order_book_level["num_orders"],
    )
    # We want to display as a list, but keep the type checking as a tuple for safety
    return cast(RestResponseOrderBookPriceLevel, list(level))


def l2_order_book_to_rest_response(l2: L2OrderBook, limit: int = 1000) -> RestResponseOrderBook:
    if limit < 2 or limit > 1000:
        raise Exception("limit must be between 2 and 1000")

    per_side = math.ceil(limit / 2)
    asks = list(map(order_book_level_to_response_level, l2["asks"][:per_side]))
    bids = list(map(order_book_level_to_response_level, l2["bids"][:per_side]))
    pool: Optional[RestResponseLiquidityPoolReserves] = (
        None
        if not l2["pool"]
        else {
            "baseReserveQuantity": pip_to_decimal(l2["pool"]["base_reserve_quantity"]),
            "quoteReserveQuantity": pip_to_decimal(l2["pool"]["quote_reserve_quantity"]),
        }
    )
    return {
        "sequence": l2["sequence"],
        "asks": asks,
        "bids": bids,
        "pool": pool,
    }


def response_level_to_order_book_level(
    level: RestResponseOrderBookPriceLevel,
) -> OrderBookLevelL2:
    return {
        "price": decimal_to_pip(level[0]),
        "size": decimal_to_pip(level[1]),
        "num_orders": level[2],
        "type": "limit",
    }


def response_to_l2_order_book(
    response: Union[RestResponseOrderBook, WebSocketResponseL2OrderBookLong]
) -> L2OrderBook:
    asks = list(map(response_level_to_order_book_level, response["asks"]))
    bids = list(map(response_level_to_order_book_level, response["bids"]))
    pool: Optional[PoolReserveQuantities] = (
        None
        if not response["pool"]
        else {
            "base_reserve_quantity": decimal_to_pip(response["pool"]["baseReserveQuantity"]),
            "quote_reserve_quantity": decimal_to_pip(response["pool"]["quoteReserveQuantity"]),
        }
    )
    return {"sequence": response["sequence"], "asks": asks, "bids": bids, "pool": pool}
