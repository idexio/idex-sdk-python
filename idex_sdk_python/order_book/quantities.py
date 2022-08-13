from decimal import ROUND_DOWN, ROUND_HALF_UP, ROUND_UP, Decimal
from typing import Callable, Dict, List, Literal, cast

from idex_sdk_python.idex_types.order_book import (
    BestAvailablePriceLevels,
    L1AndL2OrderBook,
    L2OrderBook,
    OrderBookLevelL2,
    PoolReserveQuantities,
    PriceLevelQuantities,
    SyntheticL2OrderBook,
)
from idex_sdk_python.order_book.utils import l2_to_l1_order_book
from idex_sdk_python.pipmath import (
    MAX_64_BIT_INT,
    ONE_IN_PIPS,
    divide_pips,
    multiply_pips,
    pip_to_decimal,
    square_root_big_int,
)

RoundingMode = Literal["ROUND_DOWN", "ROUND_HALF_UP", "ROUND_UP"]
ASKS_TICK_ROUNDING_MODE: RoundingMode = cast(RoundingMode, ROUND_UP)
BIDS_TICK_ROUNDING_MODE: RoundingMode = cast(RoundingMode, ROUND_DOWN)
DEFAULT_ROUNDING_MODE: RoundingMode = cast(RoundingMode, ROUND_HALF_UP)

NULL_LEVEL: OrderBookLevelL2 = {
    "price": 0,
    "size": 0,
    "num_orders": 0,
    "type": "limit",
}


def calculate_gross_base_quantity(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    target_price: int,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> int:
    """
    Helper function to calculate gross base quantity available at a bid price.
    See quantities_available_from_pool_at_bid_price.
    """
    validate_synthetic_price_level_inputs(
        base_asset_quantity, quote_asset_quantity, target_price, False
    )

    pool_fee = ONE_IN_PIPS - int((ONE_IN_PIPS * pool_fee_rate) / (ONE_IN_PIPS - idex_fee_rate))
    v0 = pool_fee * base_asset_quantity + ONE_IN_PIPS * base_asset_quantity
    v1 = base_asset_quantity * base_asset_quantity - int(
        (ONE_IN_PIPS * base_asset_quantity * quote_asset_quantity) / target_price
    )
    numerator = square_root_big_int(v0 * v0 - 4 * pool_fee * v1 * ONE_IN_PIPS) - v0
    denominator = 2 * pool_fee * (ONE_IN_PIPS - idex_fee_rate)
    return int(numerator * ONE_IN_PIPS / denominator)


def calculate_gross_base_value_of_buy_quantities(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    gross_quote_quantity: int,
) -> int:
    """
    Helper function to convert from quote to base quantities.
    See quantities_available_from_pool_at_ask_price.
    """
    return base_asset_quantity - int(
        (base_asset_quantity * quote_asset_quantity) / (quote_asset_quantity + gross_quote_quantity)
    )


def calculate_gross_quote_quantity(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    target_price: int,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> int:
    """
    Helper function to calculate gross quote available at a bid price.
    See quantities_available_from_pool_at_bid_price.
    """
    validate_synthetic_price_level_inputs(
        base_asset_quantity, quote_asset_quantity, target_price, True
    )

    pool_fee = ONE_IN_PIPS - int((ONE_IN_PIPS * pool_fee_rate) / (ONE_IN_PIPS - idex_fee_rate))
    v0 = ONE_IN_PIPS * quote_asset_quantity * (pool_fee + ONE_IN_PIPS)
    v1 = quote_asset_quantity**2 * (pool_fee**2 + 2 * pool_fee * ONE_IN_PIPS + ONE_IN_PIPS**2)
    v2 = quote_asset_quantity * (
        ONE_IN_PIPS * quote_asset_quantity - base_asset_quantity * target_price
    )

    numerator = square_root_big_int((v1 - 4 * pool_fee * v2) * ONE_IN_PIPS**2) - v0
    denominator = 2 * pool_fee * ONE_IN_PIPS - 2 * pool_fee * idex_fee_rate
    return int(numerator / denominator)


def calculate_gross_quote_value_of_sell_quantities(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    gross_base_quantity: int,
) -> int:
    """
    Helper function to convert from base to quote quantities.
    See quantities_available_from_pool_at_bid_price.
    """
    return quote_asset_quantity - int(
        (base_asset_quantity * quote_asset_quantity) / (base_asset_quantity + gross_base_quantity)
    )


def calculate_base_quantity_out(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    gross_quote_quantity_in: int,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> int:
    """
    Given a taker order size expressed in quote, how much base is received from the pool.
    See l1or_l2_best_available_prices.
    """
    if not quote_asset_quantity or not gross_quote_quantity_in:
        return 0

    numerator = base_asset_quantity * quote_asset_quantity * ONE_IN_PIPS
    denominator = quote_asset_quantity * ONE_IN_PIPS + gross_quote_quantity_in * (
        ONE_IN_PIPS - idex_fee_rate - pool_fee_rate
    )

    # The result needs to be rounded down to prevent the pool's constant product from decreasing,
    # ie. the second part of the subtraction (the division) needs to be rounded up.
    quotient = int(numerator / denominator)
    if quotient * denominator != numerator:
        quotient += 1

    return base_asset_quantity - quotient


def calculate_quote_quantity_out(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    gross_base_quantity_in: int,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> int:
    """
    Given a taker order size expressed in base, how much quote is received from the pool.
    See l1_or_l2_best_available_prices.
    """
    if not base_asset_quantity or not gross_base_quantity_in:
        return 0

    numerator = base_asset_quantity * quote_asset_quantity * ONE_IN_PIPS
    denominator = base_asset_quantity * ONE_IN_PIPS + gross_base_quantity_in * (
        ONE_IN_PIPS - idex_fee_rate - pool_fee_rate
    )

    # The result needs to be rounded down to prevent the pool's constant product from decreasing,
    # ie. the second part of the subtraction (the division) needs to be rounded up.
    quotient = int(numerator / denominator)
    if quotient * denominator != numerator:
        quotient += 1

    return quote_asset_quantity - quotient


def calculate_synthetic_price_levels(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    visible_levels: int,
    visible_slippage: int,
    idex_fee_rate: int = 0,
    pool_fee_rate: int = 0,
    tick_size: int = 1,
) -> SyntheticL2OrderBook:
    """
    Generates a synthetic orderbook consisting of price levels for pool liquidity only

    Args:
        base_asset_quantity: pool reserve in base asset, must be at least 1.0 expressed
            in pips (10^-8)
        quote_asset_quantity: pool reserve in quote asset, must be at least 1.0 expressed
            in pips (10^-8)
        visible_levels: how many ask and bid price levels to generate (of each)
        visible_slippage: how much slippage per price level, in 1/1000th of a percent (100 = 0.1%)
        idex_fee_rate: the idex fee rate to use for calculations (query /v1/exchange for current
            global setting)
        pool_fee_rate: the liquidity pool fee rate to use for calculations (query /v1/exchange for
            current global setting)
        tick_size: minimum price movement expressed in pips (10^-8)

    Returns:
        A level 2 order book with synthetic price levels only
    """
    unadjusted_pool_price = divide_pips(quote_asset_quantity, base_asset_quantity)
    pool_price = adjust_price_to_tick_size(unadjusted_pool_price, tick_size)

    # Calculate price slippage per level respecting tick size
    price_slippage_per_level = adjust_price_to_tick_size(
        int((pool_price * visible_slippage) / 100000),
        tick_size,
    )
    # If the tick size is too large compared to the price to allow for the specified slippage,
    # use the tick size itself as the slippage
    if price_slippage_per_level < tick_size:
        price_slippage_per_level = tick_size

    asks: List[OrderBookLevelL2] = []
    bids: List[OrderBookLevelL2] = []
    previous_ask_quantity_in_base = 0
    previous_bid_quantity_in_base = 0

    for level in range(1, visible_levels + 1):
        ask_price = pool_price + level * price_slippage_per_level

        ask_quantity_in_base = quantities_available_from_pool_at_ask_price(
            base_asset_quantity,
            quote_asset_quantity,
            ask_price,
            idex_fee_rate,
            pool_fee_rate,
        )["gross_base"]
        asks.append(
            {
                "price": ask_price,
                "size": ask_quantity_in_base - previous_ask_quantity_in_base,
                "num_orders": 0,
                "type": "pool",
            }
        )
        bid_price = pool_price - level * price_slippage_per_level
        if bid_price > 0:
            bid_quantity_in_base = quantities_available_from_pool_at_bid_price(
                base_asset_quantity,
                quote_asset_quantity,
                bid_price,
                idex_fee_rate,
                pool_fee_rate,
            )["gross_base"]

            bids.append(
                {
                    "price": bid_price,
                    "size": bid_quantity_in_base - previous_bid_quantity_in_base,
                    "num_orders": 0,
                    "type": "pool",
                }
            )

            previous_bid_quantity_in_base = bid_quantity_in_base

        previous_ask_quantity_in_base = ask_quantity_in_base

    return {
        "asks": asks,
        "bids": bids,
        "pool": {
            "base_reserve_quantity": base_asset_quantity,
            "quote_reserve_quantity": quote_asset_quantity,
        },
    }


def _recalculate_hybrid_level_amounts_for_side(
    orderbook: L2OrderBook,
    side: Literal["asks", "bids"],
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> None:
    if not orderbook["pool"]:
        return

    quantities_available_from_pool_func = (
        quantities_available_from_pool_at_ask_price
        if side == "asks"
        else quantities_available_from_pool_at_bid_price
    )

    def recalculate_size_for_limit(level: OrderBookLevelL2) -> None:
        assert orderbook["pool"]

        level["size"] += quantities_available_from_pool_func(
            orderbook["pool"]["base_reserve_quantity"],
            orderbook["pool"]["quote_reserve_quantity"],
            level["price"],
            idex_fee_rate,
            pool_fee_rate,
        )["gross_base"] - (
            0
            if not prev_level["price"]
            else quantities_available_from_pool_func(
                orderbook["pool"]["base_reserve_quantity"],
                orderbook["pool"]["quote_reserve_quantity"],
                prev_level["price"],
                idex_fee_rate,
                pool_fee_rate,
            )["gross_base"]
        )

    def recalculate_size_for_pool(level: OrderBookLevelL2) -> None:
        assert orderbook["pool"]
        level["size"] = (
            quantities_available_from_pool_func(
                orderbook["pool"]["base_reserve_quantity"],
                orderbook["pool"]["quote_reserve_quantity"],
                level["price"],
                idex_fee_rate,
                pool_fee_rate,
            )["gross_base"]
            - quantities_available_from_pool_func(
                orderbook["pool"]["base_reserve_quantity"],
                orderbook["pool"]["quote_reserve_quantity"],
                prev_level["price"],
                idex_fee_rate,
                pool_fee_rate,
            )["gross_base"]
        )

    prev_level: OrderBookLevelL2 = {"price": 0, "size": 0, "num_orders": 0, "type": "pool"}
    for level in orderbook[side]:
        # empty asks may be represented this way
        if level["price"] == 0:
            break

        # limit levels always accrue pool liquidity from the previous level
        if level["type"] == "limit":
            recalculate_size_for_limit(level)

        # this pool level was previously subdivided
        if level["type"] == "pool" and prev_level["type"] != "pool":
            recalculate_size_for_pool(level)

        prev_level = level


def recalculate_hybrid_level_amounts(
    orderbook: L2OrderBook,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> L2OrderBook:
    """
    Recalculate price level quantities for a book previously sorted with
    sort_and_merge_levels_unadjusted

    Args:
        orderbook: an unadjusted level 2 order book as returned by {sortAndMergeLevelsUnadjusted}
        idex_fee_rate: idex fee rate to use in pool quantity calculations
        pool_fee_rate: pool fee rate to use in pool quantity calculations
    """
    if not orderbook["pool"]:
        return orderbook

    # sanity for empty order books (which may list a "0" price level)
    while orderbook["asks"] and orderbook["asks"][0]["price"] == 0:
        orderbook["asks"].pop(0)
    while orderbook["bids"] and orderbook["bids"][0]["price"] == 0:
        orderbook["bids"].pop(0)

    _recalculate_hybrid_level_amounts_for_side(orderbook, "asks", idex_fee_rate, pool_fee_rate)
    _recalculate_hybrid_level_amounts_for_side(orderbook, "bids", idex_fee_rate, pool_fee_rate)
    return orderbook


def sort_and_merge_levels_unadjusted(
    limit_order_levels: List[OrderBookLevelL2],
    synthetic_levels: List[OrderBookLevelL2],
    is_before: Callable[[OrderBookLevelL2, OrderBookLevelL2], bool],
) -> List[OrderBookLevelL2]:
    """
    Combines limit orders and synthetic price levels into an intermediate sorted state
    IMPORTANT: this function does not update price level quantities after merging

    Args:
        limit_order_levels: a level 2 orderbook with only limit orders
        synthetic_levels: a level 2 orderbook with only synthetic orders
        is_before: comparison function for sorting price levels

    Returns:
        Level 2 order book with synthetic price levels only
    """

    c: List[OrderBookLevelL2] = []
    while limit_order_levels and synthetic_levels:
        if limit_order_levels[0]["price"] == synthetic_levels[0]["price"]:
            # we can drop synthetic levels that match limit orders
            # the quantities will be recalculated
            c.append(limit_order_levels[0])
            limit_order_levels.pop(0)
            synthetic_levels.pop(0)
        elif is_before(limit_order_levels[0], synthetic_levels[0]):
            # a[0] comes first
            c.append(limit_order_levels[0])
            limit_order_levels.pop(0)
        else:
            # b[0] comes first
            c.append(synthetic_levels[0])
            synthetic_levels.pop(0)

    return c + limit_order_levels + synthetic_levels


def quantities_available_from_pool_at_ask_price(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    ask_price: int,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> PriceLevelQuantities:
    """
    Helper function to calculate the asset quantities available at a given price level
    (pool liquidity only)

    Args:
        base_asset_quantity: pool reserve in base asset, must be at least 1.0 expressed
            in pips (10^-8)
        quote_asset_quantity: pool reserve in quote asset, must be at least 1.0 expressed
            in pips (10^-8)
        ask_price: the ask price level to calculate quantities for
        idex_fee_rate: the idex fee rate to use for calculations (query /v1/exchange for
            current global setting)
        pool_fee_rate: the liquidity pool fee rate to use for calculations (query /v1/exchange for
            current global setting)

    Returns:
        Level 2 order book with synthetic price levels only
    """
    # if a limit order is equal to the pool price, the pool does not contribute
    if ask_price <= divide_pips(quote_asset_quantity, base_asset_quantity):
        return {
            "gross_base": 0,
            "gross_quote": 0,
        }

    gross_quote: int = calculate_gross_quote_quantity(
        base_asset_quantity, quote_asset_quantity, ask_price, idex_fee_rate, pool_fee_rate
    )
    idex_fee: int = multiply_pips(gross_quote, idex_fee_rate)
    pool_fee: int = multiply_pips(gross_quote, pool_fee_rate)
    net_quote: int = int(
        (gross_quote * (ONE_IN_PIPS - idex_fee_rate - pool_fee_rate)) / ONE_IN_PIPS
    )
    base_out: int = base_asset_quantity - int(
        (base_asset_quantity * quote_asset_quantity) / (quote_asset_quantity + net_quote)
    )

    # new pool balances, including the retained pool fee
    resulting_base: int = base_asset_quantity - base_out
    resulting_quote: int = quote_asset_quantity + pool_fee + net_quote

    # fix quote quantity for constant pricing
    resulting_price = divide_pips(resulting_quote, resulting_base)
    if resulting_price < ask_price:
        net_quote += multiply_pips(ask_price, resulting_base, True) - resulting_quote
    elif resulting_price > ask_price:
        net_quote -= 1

    gross_quote_in = net_quote + pool_fee + idex_fee
    return {
        "gross_base": calculate_gross_base_value_of_buy_quantities(
            base_asset_quantity, quote_asset_quantity, gross_quote_in
        ),
        "gross_quote": gross_quote,
    }


def quantities_available_from_pool_at_bid_price(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    bid_price: int,
    idex_fee_rate: int,
    pool_fee_rate: int,
) -> PriceLevelQuantities:
    """
    Helper function to calculate the asset quantities available at a given price level
    (pool liquidity only)

    Args:
        base_asset_quantity: pool reserve in base asset, must be at least 1.0
            expressed in pips (10^-8)
        quote_asset_quantity: pool reserve in quote asset, must be at least 1.0
            expressed in pips (10^-8)
        bid_price: the bid price level to calculate quantities for
        idex_fee_rate: the idex fee rate to use for calculations (query /v1/exchange for
            current global setting)
        pool_fee_rate: the liquidity pool fee rate to use for calculations (query /v1/exchange for
            current global setting)

    Returns:
        Level 2 order book with synthetic price levels only
    """
    # if a limit order is equal to the pool price, the pool does not contribute
    if bid_price >= divide_pips(quote_asset_quantity, base_asset_quantity):
        return {
            "gross_base": 0,
            "gross_quote": 0,
        }

    gross_base = calculate_gross_base_quantity(
        base_asset_quantity,
        quote_asset_quantity,
        bid_price,
        idex_fee_rate,
        pool_fee_rate,
    )

    return {
        "gross_base": gross_base,
        "gross_quote": calculate_gross_quote_value_of_sell_quantities(
            base_asset_quantity, quote_asset_quantity, gross_base
        ),
    }


def aggregate_l2_order_book_at_tick_size(input_book: L2OrderBook, tick_size: int) -> L2OrderBook:
    """
    Helper function to re-aggregate L2 orderbook price levels at a larger (more zeroes) tick size
    """
    ask_levels_by_price: Dict[int, OrderBookLevelL2] = {}
    for ask_level in input_book["asks"]:
        price = adjust_price_to_tick_size(ask_level["price"], tick_size, ASKS_TICK_ROUNDING_MODE)
        level = ask_levels_by_price.get(price)
        if not level:
            level = NULL_LEVEL.copy()
            level["price"] = price
        level["num_orders"] += ask_level["num_orders"]
        level["size"] += ask_level["size"]
        ask_levels_by_price[price] = level

    bid_levels_by_price: Dict[int, OrderBookLevelL2] = {}
    for bid_level in input_book["bids"]:
        price = adjust_price_to_tick_size(bid_level["price"], tick_size, BIDS_TICK_ROUNDING_MODE)
        level = bid_levels_by_price.get(price)
        if not level:
            level = NULL_LEVEL.copy()
            level["price"] = price
        level["num_orders"] += bid_level["num_orders"]
        level["size"] += bid_level["size"]
        bid_levels_by_price[price] = level

    return {
        "sequence": input_book["sequence"],
        "asks": list(ask_levels_by_price.values()),
        "bids": list(bid_levels_by_price.values()),
        "pool": input_book["pool"],
    }


def l1_best_available_buy_price(
    pool: PoolReserveQuantities,
    idex_fee_rate: int,
    pool_fee_rate: int,
    taker_minimum_in_quote: int,
    tick_size: int,
) -> int:
    taker_minimum_in_quote_after_idex_fee = multiply_pips(
        taker_minimum_in_quote,
        ONE_IN_PIPS - idex_fee_rate,
    )
    base_received = calculate_base_quantity_out(
        pool["base_reserve_quantity"],
        pool["quote_reserve_quantity"],
        taker_minimum_in_quote,
        idex_fee_rate,
        pool_fee_rate,
    )

    return adjust_price_to_tick_size(
        divide_pips(
            pool["quote_reserve_quantity"] + taker_minimum_in_quote_after_idex_fee,
            pool["base_reserve_quantity"] - base_received,
        ),
        tick_size,
        ASKS_TICK_ROUNDING_MODE,
    )


def l1_best_available_sell_price(
    pool: PoolReserveQuantities,
    idex_fee_rate: int,
    pool_fee_rate: int,
    taker_minimum_in_base: int,
    tick_size: int,
) -> int:
    taker_minimum_in_base_after_idex_fee = multiply_pips(
        taker_minimum_in_base,
        ONE_IN_PIPS - idex_fee_rate,
    )
    quote_received = calculate_quote_quantity_out(
        pool["base_reserve_quantity"],
        pool["quote_reserve_quantity"],
        taker_minimum_in_base,
        idex_fee_rate,
        pool_fee_rate,
    )

    return adjust_price_to_tick_size(
        divide_pips(
            pool["quote_reserve_quantity"] - quote_received,
            pool["base_reserve_quantity"] + taker_minimum_in_base_after_idex_fee,
        ),
        tick_size,
        BIDS_TICK_ROUNDING_MODE,
    )


def l1_or_l2_best_available_prices(
    pool: PoolReserveQuantities,
    idex_fee_rate: int,
    pool_fee_rate: int,
    taker_minimum_in_base: int,
    taker_minimum_in_quote: int,
    tick_size: int,
) -> BestAvailablePriceLevels:
    """
    Given a minimum taker order size, calculate the best achievable price level using
    pool liquidity only.

    Args:
        pool: pool reserve quantities for the orderbook in question
        idex_fee_rate: the idex fee rate to use for pool calculations
        pool_fee_rate: the pool fee rate to use for pool calculations
        taker_minimum_in_base: the minimum taker order size, expressed in base asset units
        taker_minimum_in_quote: the minimum taker order size, expressed in quote asset units
    """
    return {
        "buy_price": l1_best_available_buy_price(
            pool,
            idex_fee_rate,
            pool_fee_rate,
            taker_minimum_in_quote,
            tick_size,
        ),
        "sell_price": l1_best_available_sell_price(
            pool,
            idex_fee_rate,
            pool_fee_rate,
            taker_minimum_in_base,
            tick_size,
        ),
    }


def l1_l2_order_books_with_minimum_taker(
    l2: L2OrderBook,
    idex_fee_rate: int,
    pool_fee_rate: int,
    taker_minimum_in_quote: int,
    tick_size: int,
) -> L1AndL2OrderBook:
    """
    Modifies an existing level 2 order book to include better price levels at the desired taker
    order size, if available from pool reserves.

    Args:
        pool: pool reserve quantities for the orderbook in question
        idexFeeRate: the idex fee rate to use for pool calculations
        poolFeeRate: the pool fee rate to use for pool calculations
        takerMinimumInQuote: the minimum taker order size, expressed in quote asset units

    Returns:
        The resulting level 1 and level 2 orderbooks
    """
    if not l2["pool"]:
        return {"l1": l2_to_l1_order_book(l2), "l2": l2}

    l2_values: L2OrderBook = l2.copy()
    taker_minimum_in_base = int(
        taker_minimum_in_quote
        * l2["pool"]["base_reserve_quantity"]
        / l2["pool"]["quote_reserve_quantity"]
    )

    best_available_prices = l1_or_l2_best_available_prices(
        l2["pool"],
        idex_fee_rate,
        pool_fee_rate,
        taker_minimum_in_base,
        taker_minimum_in_quote,
        tick_size,
    )
    buy_price = best_available_prices["buy_price"]
    sell_price = best_available_prices["sell_price"]

    gross_buy_base = quantities_available_from_pool_at_ask_price(
        l2["pool"]["base_reserve_quantity"],
        l2["pool"]["quote_reserve_quantity"],
        buy_price,
        idex_fee_rate,
        pool_fee_rate,
    )["gross_base"]

    if gross_buy_base < taker_minimum_in_base:
        buy_price += tick_size
        gross_buy_base = quantities_available_from_pool_at_ask_price(
            l2["pool"]["base_reserve_quantity"],
            l2["pool"]["quote_reserve_quantity"],
            buy_price,
            idex_fee_rate,
            pool_fee_rate,
        )["gross_base"]

    if not l2["asks"] or buy_price < l2["asks"][0]["price"]:
        l2_values["asks"].insert(
            0, {"price": buy_price, "size": gross_buy_base, "num_orders": 0, "type": "pool"}
        )
        if len(l2_values["asks"]) > 1:
            l2_values["asks"][1]["size"] -= gross_buy_base

    # Best sell price will be 0 in case there are no bids
    if sell_price > 0:
        gross_sell_base = quantities_available_from_pool_at_bid_price(
            l2["pool"]["base_reserve_quantity"],
            l2["pool"]["quote_reserve_quantity"],
            sell_price,
            idex_fee_rate,
            pool_fee_rate,
        )["gross_base"]

        if gross_sell_base < taker_minimum_in_base:
            sell_price -= tick_size
            gross_sell_base = quantities_available_from_pool_at_bid_price(
                l2["pool"]["base_reserve_quantity"],
                l2["pool"]["quote_reserve_quantity"],
                sell_price,
                idex_fee_rate,
                pool_fee_rate,
            )["gross_base"]

        if not l2["bids"] or sell_price > l2["bids"][0]["price"]:
            l2_values["bids"].insert(
                0, {"price": sell_price, "size": gross_sell_base, "num_orders": 0, "type": "pool"}
            )
            if len(l2_values["bids"]) > 1:
                l2_values["bids"][1]["size"] -= gross_sell_base

    return {"l1": l2_to_l1_order_book(l2_values), "l2": l2_values}


def validate_synthetic_price_level_inputs(
    base_asset_quantity: int,
    quote_asset_quantity: int,
    target_price: int,
    is_buy: bool,
) -> None:
    """
    Validates assumptions for reserve quantities and pricing required for quantity calculations

    Args:
        base_asset_quantity: pool reserve in base asset, must be at least 1.0 expressed
            in pips (10^-8)
        quote_asset_quantity: pool reserve in quote asset, must be at least 1.0 expressed
            in pips (10^-8)
        target_price: price expressed in pips, must be 0 < price < 2^64-1 and on the correct side
            of the spread
        is_buy: if true, the price is targeting buy orders (bids), otherwise sell orders (asks)

    Returns:
        None, validation always succeeds or raises an exception
    """
    if base_asset_quantity < ONE_IN_PIPS or quote_asset_quantity < ONE_IN_PIPS:
        raise Exception(
            "Base asset quantity and quote asset quantity must be positive integers, "
            "for pools with at least 1 quote and 1 base token"
        )

    if target_price <= 0 or target_price > MAX_64_BIT_INT:
        raise Exception(
            f"Target price ({pip_to_decimal(target_price)}) "
            "must be above zero and below the 64 bit integer limit"
        )

    current_price = divide_pips(quote_asset_quantity, base_asset_quantity)
    if is_buy and current_price >= target_price:
        raise Exception(
            f"Target price ({pip_to_decimal(target_price)}) must be above "
            f"the current price ({pip_to_decimal(current_price)})"
        )
    if not is_buy and current_price <= target_price:
        raise Exception(
            f"Target price ({pip_to_decimal(target_price)}) must be below "
            f"the current price ({pip_to_decimal(current_price)})"
        )


def adjust_price_to_tick_size(
    price: int,
    tick_size: int,
    rounding_mode: RoundingMode = DEFAULT_ROUNDING_MODE,
) -> int:
    """
    Adjusts prices in pips to account for tick size by discarding insignificant digits using
    specified rounding mode. Ex price 123456789 at tick size 1 is 123456789, at tick size 10
    123456780, at 100 123456700, etc
    """
    significant_digits: float = price / tick_size

    rounded_significant_digits: int = int(
        Decimal(significant_digits).to_integral_value(rounding=rounding_mode)
    )
    return rounded_significant_digits * tick_size
