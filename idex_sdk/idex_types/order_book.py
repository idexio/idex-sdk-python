from typing import List, Literal, Optional, TypedDict


class BestAvailablePriceLevels(TypedDict):
    buy_price: int
    sell_price: int


class OrderBookFeesAndMinimums(TypedDict):
    """
    Attributes:
        takerIdexFeeRate: Taker trade fee rate collected by IDEX; used in computing synthetic
            price levels for real-time order book
        takerLiquidityProviderFeeRate: Taker trade fee rate collected by liquidity providers; used
            in computing synthetic price levels for real-time order book
        takerTradeMinimum: Minimum order size that is accepted by the matching engine for
            execution in MATIC, applies to both MATIC and token
    """

    taker_idex_fee_rate: str
    taker_liquidity_provider_fee_rate: str
    taker_trade_minimum: str


OrderBookLevelType = Literal["limit", "pool"]


class OrderBookLevelL1(TypedDict):
    price: int
    size: int
    num_orders: int


class OrderBookLevelL2(OrderBookLevelL1):
    type: OrderBookLevelType


class PoolReserveQuantities(TypedDict):
    base_reserve_quantity: int
    quote_reserve_quantity: int


class PriceLevelQuantities(TypedDict):
    gross_base: int
    gross_quote: int


class L1OrderBook(TypedDict):
    sequence: int
    asks: OrderBookLevelL1
    bids: OrderBookLevelL1
    pool: Optional[PoolReserveQuantities]


class L2OrderBook(TypedDict):
    sequence: int
    asks: List[OrderBookLevelL2]
    bids: List[OrderBookLevelL2]
    pool: Optional[PoolReserveQuantities]


class SyntheticL2OrderBook(TypedDict):
    asks: List[OrderBookLevelL2]
    bids: List[OrderBookLevelL2]
    pool: Optional[PoolReserveQuantities]


class L1AndL2OrderBook(TypedDict):
    l1: L1OrderBook
    l2: L2OrderBook
