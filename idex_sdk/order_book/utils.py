from idex_sdk.idex_types.order_book import L1OrderBook, L2OrderBook


def l2_to_l1_order_book(l2: L2OrderBook) -> L1OrderBook:
    """
    Derive the level 1 orderbook from a level 2 orderbook
    """
    return {
        "sequence": l2["sequence"],
        "asks": (
            {
                "price": l2["asks"][0]["price"],
                "size": l2["asks"][0]["size"],
                "num_orders": l2["asks"][0]["num_orders"],
            }
            if l2["asks"]
            else {"price": 0, "size": 0, "num_orders": 0}
        ),
        "bids": (
            {
                "price": l2["bids"][0]["price"],
                "size": l2["bids"][0]["size"],
                "num_orders": l2["bids"][0]["num_orders"],
            }
            if l2["bids"]
            else {"price": 0, "size": 0, "num_orders": 0}
        ),
        "pool": l2["pool"],
    }
