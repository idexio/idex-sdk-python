from enum import Enum
from typing import Dict, Literal

# The available candle time intervals
CandleInterval = Literal[
    "1m",
    "5m",
    "15m",
    "30m",
    "1h",
    "6h",
    "1d",
]


# The available eth transaction status options
EthTransactionStatus = Literal[
    "pending",
    "mined",
    "failed",
]
ETH_TRANSACTION_STATUS_IDS: Dict[EthTransactionStatus, int] = {
    "pending": 0,
    "mined": 1,
    "failed": 2,
}


# The available liquidity options
Liquidity = Literal[
    # Maker provides liquidity
    "maker",
    # Taker removes liquidity
    "taker",
]
LIQUIDITY_IDS: Dict[Liquidity, int] = {
    "maker": 0,
    "taker": 1,
}


# The available market status options
MarketStatus = Literal[
    # No orders or cancels accepted
    "inactive",
    # Cancels accepted but not trades
    "cancelsOnly",
    # Cancels and limit maker orders only
    "limitMakerOnly",
    # Trades and cancels accepted
    "active",
    # Hybrid trades and cancels accepted
    "activeHybrid",
]

# The available market type options
MarketType = Literal[
    # Orderbook trades accepted
    "orderBook",
    # Orderbook, pool, and hybrid trades accepted
    "hybrid",
]


# The available liquidity change origination options
class LiquidityChangeOrigination(Enum):
    # Initiation on-chain via contract call
    ONCHAIN = 0
    # Initiation off-chain via API
    OFFCHAIN = 1


# The available liquidity change type options
class LiquidityChangeType(Enum):
    # Adding reserve assets to pool and minting LP tokens
    ADDITION = 0
    # Removing reserve assets from pool and burning LP tokens
    REMOVAL = 1


# The available multiverse chains to define when creating a client
class MultiverseChain(Enum):
    MATIC = "matic"


# The available order signature hash versions
# OrderSignatureHashVersion = Literal[4, 104]
class OrderSignatureHashVersion(Enum):
    MATIC = 4
    MATIC_SANDBOX = 104


# The available order self-trade prevention options
OrderSelfTradePrevention = Literal[
    # Decrement And Cancel (DC) - When two orders from the same user cross, the smaller order will
    # be canceled and the larger order size will be decremented by the smaller order size.
    # If the two orders are the same size, both will be canceled.
    "dc",
    # Cancel Oldest (CO) - Cancel the older (maker) order in full
    "co",
    # Cancel Newest (CN) - Cancel the newer, taker order and leave the older, resting order on
    # the order book. This is the only valid option when time-in-force is set to fill or kill.
    "cn",
    # Cancel Both (CB) - Cancel both orders
    "cb",
]
ORDER_SELF_TRADE_PREVENTION_IDS: Dict[OrderSelfTradePrevention, int] = {
    "dc": 0,
    "co": 1,
    "cn": 2,
    "cb": 3,
}

# The available order side options
OrderSide = Literal["buy", "sell"]
ORDER_SIDE_IDS: Dict[OrderSide, int] = {
    "buy": 0,
    "sell": 1,
}


# The available order state change options
OrderStateChange = Literal[
    # An order without a stop has been accepted into the trading engine.
    # Will not be sent as a discrete change event if the order matches on execution.
    "new",
    # A stop order has accepted into the trading engine, once triggered,
    # will go through other normal events starting with new
    "activated",
    # An order has generated a fill, both on maker and taker sides.
    # Will be the first change event sent if an order matches on execution.
    "fill",
    # An order is canceled by the user.
    "canceled",
    # LIMIT FOK orders with no fill, LIMIT IOC or MARKET orders that partially fill,
    # GTT orders past time.
    "expired",
]
ORDER_STATE_CHANGE_IDS: Dict[OrderStateChange, int] = {
    "new": 0,
    "activated": 1,
    "fill": 2,
    "canceled": 3,
    "expired": 4,
}


# The available order status options
OrderStatus = Literal[
    # Stop order exists on the order book
    "active",
    # Limit order exists on the order book
    "open",
    # Limit order has completed fills but has remaining open quantity
    "partiallyFilled",
    # Limit order is completely filled and is no longer on the book; market order was filled
    "filled",
    # Limit order was canceled prior to execution completion but may be partially filled
    "cancelled",
    # Order was rejected by the trading engine
    "rejected",
    # GTT limit order expired prior to execution completion but may be partially filled
    "expired",
    # Order submitted to the test endpoint and accepted by the trading engine, not executed
    "testOnlyAccepted",
    # Order submitted to the test endpoint and rejected by validation or the trading
    # engine, not executed
    "testOnlyRejected",
]
ORDER_STATUS_IDS: Dict[OrderStatus, int] = {
    "active": 0,
    "open": 1,
    "partiallyFilled": 2,
    "filled": 3,
    "cancelled": 4,
    "rejected": 5,
    "expired": 6,
    "testOnlyAccepted": 7,
    "testOnlyRejected": 8,
}


# The available order time-in-force options
OrderTimeInForce = Literal[
    # Good until canceled (default)
    "gtc",
    # Good until time
    "gtt",
    # Immediate or cancel
    "ioc",
    # Fill or kill
    "fok",
]
ORDER_TIME_IN_FORCE_IDS: Dict[OrderTimeInForce, int] = {
    "gtc": 0,
    "gtt": 1,
    "ioc": 2,
    "fok": 3,
}


# The available order type options
OrderType = Literal[
    "market",
    "limit",
    "limitMaker",
    "stopLoss",
    "stopLossLimit",
    "takeProfit",
    "takeProfitLimit",
]
ORDER_TYPE_IDS: Dict[OrderType, int] = {
    "market": 0,
    "limit": 1,
    "limitMaker": 2,
    "stopLoss": 3,
    "stopLossLimit": 4,
    "takeProfit": 5,
    "takeProfitLimit": 6,
}


# The available trade type options
TradeType = Literal["orderBook", "pool", "hybrid"]
TRADE_TYPE_IDS: Dict[TradeType, int] = {"orderBook": 0, "pool": 1, "hybrid": 2}
