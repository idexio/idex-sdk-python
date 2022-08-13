from typing import List

from idex_sdk_python.idex_types.order_book import (
    L1OrderBook,
    L2OrderBook,
    OrderBookLevelL2,
)


def l1_equal(before_l1: L1OrderBook, after_l1: L1OrderBook) -> bool:
    """Determine whether two level 1 order books are equal, including pool reserves"""
    return (
        before_l1["asks"] == after_l1["asks"]
        and before_l1["bids"] == after_l1["bids"]
        and before_l1["pool"] == after_l1["pool"]
    )


def update_l2_side(
    is_ascending: bool, side: List[OrderBookLevelL2], updates: List[OrderBookLevelL2]
) -> List[OrderBookLevelL2]:
    """
    Applies a changeset to a single side of the orderbook

    Params:
        is_ascending: true for asks, false for bids (ordering of price levels)
        side
        updates

    Returns:
        Updated order book side
    """

    def is_before_or_equal(a: OrderBookLevelL2, b: OrderBookLevelL2) -> bool:
        if is_ascending and a["price"] <= b["price"]:
            return True
        if not is_ascending and a["price"] >= b["price"]:
            return True
        return False

    next_update = updates.pop(0) if updates else None
    if not next_update:
        return side

    last_price_updated = 0
    new_levels: List[OrderBookLevelL2] = []

    for level in side:
        # Push all updated price levels prior to the existing level.
        # Skip any with no size and no orders.
        while next_update and is_before_or_equal(next_update, level):
            if next_update["size"] and next_update["num_orders"]:
                new_levels.append(next_update)
            last_price_updated = next_update["price"]
            next_update = updates.pop(0) if updates else None
        if level["price"] != last_price_updated:
            new_levels.append(level)

    while next_update and next_update["size"] and next_update["num_orders"]:
        new_levels.append(next_update)
        next_update = updates.pop(0) if updates else None

    return new_levels


def update_l2_levels(book: L2OrderBook, updated_levels: L2OrderBook) -> None:
    """
    Updates a level 2 orderbook using a partial "diff" received over websockets

    Args:
        book: level 2 orderbook to update
        updated_levels: level 2 orderbook containing only limit order price levels that
            have changed
    """
    book["sequence"] = updated_levels["sequence"]
    book["asks"] = update_l2_side(True, book["asks"], updated_levels["asks"])
    book["bids"] = update_l2_side(False, book["bids"], updated_levels["bids"])
    book["pool"] = updated_levels["pool"]
    pass
