from typing import Optional

from idex_sdk_python.idex_types.order_book import L1AndL2OrderBook, L2OrderBook
from idex_sdk_python.order_book.quantities import (
    calculate_synthetic_price_levels,
    l1_l2_order_books_with_minimum_taker,
    recalculate_hybrid_level_amounts,
    sort_and_merge_levels_unadjusted,
)
from idex_sdk_python.order_book.utils import l2_to_l1_order_book


def l2_limit_order_book_to_hybrid_order_books(
    order_book: L2OrderBook,
    idex_fee_rate: int,
    pool_fee_rate: int,
    include_minimum_taker_levels: bool,
    minimum_taker_in_quote: Optional[int],
    tick_size: int,
    visible_levels: int = 10,
    visible_slippage: int = 100,
) -> L1AndL2OrderBook:
    """
    Convert a limit-order orderbook and a liquidity pool to a hybrid order book representation

    Args:
        order_book: L2 book, e.g. from GET /v1/orderbook?level=2&limitOrderOnly=true
        visible_levels: number of price levels to calculate, default = 10 asks, 10 bids
        visible_slippage: price slippage per level, in increments of 0.001%, default = 100 (0.1%)
        idex_fee_rate: trade fee rate charged by IDEX, expressed in pips
        pool_fee_rate: pool fee rate chared by liquidity pool, expressed in pips
        include_minimum_taker_levels: if true, calculate a synthetic price level at twice
            the minimum trade size
        minimum_taker_in_quote: minimum trade size expressed in pips, or null if none available
        tick_size: minimum price movement expressed in pips (10^-8)
    """
    if not order_book["pool"]:
        return {"l1": l2_to_l1_order_book(order_book), "l2": order_book}

    synthetic = calculate_synthetic_price_levels(
        order_book["pool"]["base_reserve_quantity"],
        order_book["pool"]["quote_reserve_quantity"],
        visible_levels,
        visible_slippage,
        idex_fee_rate,
        pool_fee_rate,
        tick_size,
    )

    # Synthetic price level constraints could not be satisfied, return unadjusted orderbook
    if not synthetic:
        return {"l1": l2_to_l1_order_book(order_book), "l2": order_book}

    # need to make a deep copy of asks and bids because they will be modified
    limit_asks_copy = list(map(lambda order: order.copy(), order_book["asks"]))
    limit_bids_copy = list(map(lambda order: order.copy(), order_book["bids"]))

    adjusted_l2_order_book = recalculate_hybrid_level_amounts(
        {
            "sequence": order_book["sequence"],
            "asks": sort_and_merge_levels_unadjusted(
                limit_asks_copy,
                synthetic["asks"],
                lambda a, b: a["price"] <= b["price"],
            ),
            "bids": sort_and_merge_levels_unadjusted(
                limit_bids_copy,
                synthetic["bids"],
                lambda a, b: a["price"] >= b["price"],
            ),
            "pool": {
                "base_reserve_quantity": order_book["pool"]["base_reserve_quantity"],
                "quote_reserve_quantity": order_book["pool"]["quote_reserve_quantity"],
            },
        },
        idex_fee_rate,
        pool_fee_rate,
    )

    if include_minimum_taker_levels and minimum_taker_in_quote and minimum_taker_in_quote > 0:
        return l1_l2_order_books_with_minimum_taker(
            adjusted_l2_order_book,
            idex_fee_rate,
            pool_fee_rate,
            minimum_taker_in_quote,
            tick_size,
        )
    else:
        return {"l1": l2_to_l1_order_book(adjusted_l2_order_book), "l2": adjusted_l2_order_book}
