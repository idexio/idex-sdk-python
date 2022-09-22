from typing import List, Literal, Optional, TypedDict, Union

from idex_sdk.idex_types.enums import (
    CandleInterval,
    EthTransactionStatus,
    Liquidity,
    OrderSelfTradePrevention,
    OrderSide,
    OrderStateChange,
    OrderStatus,
    OrderTimeInForce,
    OrderType,
    TradeType,
)
from idex_sdk.idex_types.rest import response as rest_response
from idex_sdk.idex_types.websocket.request import WebSocketRequestSubscription

# tickers


class WebSocketResponseTickerShort(TypedDict):
    """
    Attributes:
        m: (market) Market symbol
        t: (time) Timestamp when the statistics were computed, the opening time of the period is
            24 hours prior
        o: (open) Price of the first trade in the period in quote terms
        h: (high) Highest traded price in the period in quote terms
        l: (low) Lowest traded price in the period in quote terms
        c: (close) Price of the last trade in the period in quote terms
        Q: (closeQuantity) Quantity of the last trade in th period in base terms
        v: (baseVolume) Trailing 24-hour trading volume in base terms
        q: (quoteVolume) Trailing 24-hour trading volume in quote terms
        P: (percentChange) Percentage change from open price to close price
        n: (numTrades) Number of trades in the period
        a: (ask) Best ask price on the order book in quote terms
        b: (bid) Best bid price on the order book in quote terms
        u: (sequence) Fill sequence number of the last trade in the period
    """

    m: str
    t: int
    o: Optional[str]
    h: Optional[str]
    l: Optional[str]
    c: Optional[str]
    Q: Optional[str]
    v: str
    q: str
    P: str
    n: int
    a: Optional[str]
    b: Optional[str]
    u: Optional[int]


WebSocketResponseTickerLong = rest_response.RestResponseTicker


# candles


class WebSocketResponseCandleShort(TypedDict):
    """
    Attributes:
        m: (market) Market symbol
        t: (time) Timestamp when the statistics were computed, time is always between the start
            and end timestamps of the interval
        i: (interval) Interval duration, see Interval Values
        s: (start) Timestamp of the start of the interval
        e: (end) Timestamp of the end of the interval
        o: (open) Price of the first trade in the interval in quote terms
        h: (high) Highest traded price in the interval in quote terms
        l: (low) Lowest traded price in the interval in quote terms
        c: (close) Price of the last trade in the interval in quote terms
        v: (volume) Trading volume in the interval in base terms
        n: (numTrades) Number of trades in the candle
        u: (sequence) Fill sequence number of the last trade in the interval
    """

    m: str
    t: int
    i: CandleInterval
    s: int
    e: int
    o: str
    h: str
    l: str
    c: str
    v: str
    n: int
    u: int


class WebSocketResponseCandleLong(rest_response.RestResponseCandle):
    """
    Attributes:
        market: Market symbol
        time: Timestamp when the statistics were computed, time is always between the start and
            end timestamps of the interval
        interval: Interval duration, see Interval Values
        start: Timestamp of the start of the interval
        end: Timestamp of the end of the interval
        open: Price of the first trade in the interval in quote terms
        high: Highest traded price in the interval in quote terms
        low: Lowest traded price in the interval in quote terms
        close: Price of the last trade in the interval in quote terms
        volume: Trading volume in the interval in base terms
        numTrades: Number of trades in the candle
        sequence: Fill sequence number of the last trade in the interval
    """

    market: str
    time: int
    interval: CandleInterval
    end: int
    numTrades: int


#  trades


class WebSocketResponseTradeShort(TypedDict):
    """
    Attributes:
        y: (type) orderBook, pool, or hybrid
        m: (market) Market symbol
        i: (fillId) Trade identifier
        p: (price) Price of the trade in quote terms
        q: (quantity) Quantity of the trade in base terms
        Q: (quoteQuantity) Quantity of the trade in quote terms
        t: (time) Timestamp of the trade
        s: (makerSide) Maker side of the trade, buy or sell
        u: (sequence) Fill sequence number of the trade
    """

    y: TradeType
    m: str
    i: str
    p: str
    q: str
    Q: str
    t: int
    s: OrderSide
    u: int


class WebSocketResponseTradeLong(rest_response.RestResponseTrade):
    market: str


# liquidity


class WebSocketResponseLiquidityPoolShort(TypedDict):
    """
    Attributes:
        q: (baseReserveQuantity) quantity of base asset held in the liquidity pool
        Q: (quoteReserveQuantity) quantity of quote asset held in the liquidity pool
    """

    q: str
    Q: str


class WebSocketResponseLiquidityPoolLong(TypedDict):
    """
    Attributes:
        baseReserveQuantity: quantity of base asset held in the liquidity pool
        quoteReserveQuantity: quantity of quote asset held in the liquidity pool
    """

    baseReserveQuantity: str
    quoteReserveQuantity: str


# l1orderbook


class WebSocketResponseL1OrderBookShort(TypedDict):
    """
    Attributes:
        m: (market) Market symbol
        t: (time) Timestamp of the order book update
        b: (bidPrice) Best bid price
        B: (bidQuantity) Quantity available at the best bid price
        a: (askPrice) Best ask price
        A: (askQuantity) Quantity available at the best ask price
        p: Liquidity pool reserves for this market
    """

    m: str
    t: int
    b: str
    B: str
    a: str
    A: str
    p: Optional[WebSocketResponseLiquidityPoolShort]


class WebSocketResponseL1OrderBookLong(TypedDict):
    """
    Attributes:
        market: Market symbol
        time: Timestamp of the order book update
        bidPrice: Best bid price
        bidQuantity: Quantity available at the best bid price
        askPrice: Best ask price
        askQuantity: Quantity available at the best ask price
        pool: Liquidity pool reserves for this market
    """

    market: str  # m
    time: int  # t
    bidPrice: str  # b
    bidQuantity: str  # B
    askPrice: str  # a
    askQuantity: str  # A
    pool: Optional[WebSocketResponseLiquidityPoolLong]  # p


# l2orderbook


WebSocketResponseL2OrderBookChange = rest_response.RestResponseOrderBookPriceLevel


class WebSocketResponseL2OrderBookShort(TypedDict):
    """
    Attributes:
        m: (market) Market symbol
        t: (time) Timestamp of the order book update
        u: (sequence) Order book update sequence number of the update
        b: (bids) Array of bid price level updates
        a: (asks) Array of ask price level updates
        p: Liquidity pool reserves for this market
    """

    m: str
    t: int
    u: int
    b: List[WebSocketResponseL2OrderBookChange]
    a: List[WebSocketResponseL2OrderBookChange]
    p: Optional[WebSocketResponseLiquidityPoolShort]


class WebSocketResponseL2OrderBookLong(TypedDict):
    """
    Attributes:
        market: Market symbol
        time: Timestamp of the order book update
        sequence: Order book update sequence number of the update
        bids: Array of bid price level updates
        asks: Array of ask price level updates
        pool: liquidity pool reserves
        p: Liquidity pool reserves for this market
    """

    market: str  # m
    time: int  # t
    sequence: int  # u
    bids: List[WebSocketResponseL2OrderBookChange]  # b
    asks: List[WebSocketResponseL2OrderBookChange]  # a
    pool: Optional[WebSocketResponseLiquidityPoolLong]  # p


# balances


class WebSocketResponseBalanceShort(TypedDict):
    """
    Attributes:
        w: (wallet) Target wallet address
        a: (asset) Asset symbol
        q: (quantity) Total quantity of the asset held by the wallet on the exchange
        f: (availableForTrade) Quantity of the asset available for trading; quantity: locked
        l: (locked) Quantity of the asset held in trades on the order book
        d: (usdValue) Total value of the asset held by the wallet on the exchange in USD
    """

    w: str
    a: str
    q: str
    f: str
    l: str
    d: str


class WebSocketResponseBalanceLong(TypedDict):
    """
    Attributes:
        wallet: Target wallet address
        asset: Asset symbol
        quantity: Total quantity of the asset held by the wallet on the exchange
        availableForTrade: Quantity of the asset available for trading; quantity: locked
        locked: Quantity of the asset held in trades on the order book
        usdValue: Total value of the asset held by the wallet on the exchange in USD
    """

    wallet: str  # w
    asset: str  # a
    quantity: str
    availableForTrade: str  # f
    locked: str  # l
    usdValue: str  # d


# orders


class _WebSocketResponseOrderFillShortRequiredAttribs(TypedDict):
    y: TradeType
    i: str
    p: str
    q: str
    Q: str
    t: int
    s: OrderSide
    u: int
    f: str
    a: str
    l: Liquidity
    T: Optional[str]
    S: EthTransactionStatus


class WebSocketResponseOrderFillShort(_WebSocketResponseOrderFillShortRequiredAttribs, total=False):
    """
    Attributes:
        i: (fillId) Fill identifier
        p: (price) Price of the fill in quote terms
        q: (quantity) Quantity of the fill in base terms
        Q: (quoteQuantity) Quantity of the fill in quote terms
        oq: Quantity of the fill in base terms supplied by order book liquidity, omitted
            for pool fills
        oQ: Quantity of the fill in quote terms supplied by order book liquidity, omitted
            for pool fills
        pq: Quantity of the fill in base terms supplied by pool liquidity, omitted
            for orderBook fills
        pQ: Quantity of the fill in quote terms supplied by pool liquidity, omitted
            for orderBook fills
        t: (time) Timestamp of the fill
        s: (makerSide) Maker side of the fill, buy or sell
        u: (sequence) Fill sequence number
        f: (fee) Fee amount collected on the fill
        a: (feeAsset) Symbol of asset in which fees collected
        g: (gas) Amount collected to cover trade settlement gas costs, only present for taker
        l: (liquidity) Whether the fill is the maker or taker in the trade from the perspective of
            the requesting user account, maker or taker
        T: (txId) Ethereum ID of the trade settlement transaction
        S: (txStatus) Status of the trade settlement transaction, see values
    """

    oq: str
    oQ: str
    pq: str
    pQ: str
    g: str


WebSocketResponseOrderFillLong = rest_response.RestResponseOrderFill


class _WebSocketResponseOrderShortRequiredAttribs(TypedDict):
    m: str
    i: str
    w: str
    t: int
    T: int
    x: OrderStateChange
    X: OrderStatus
    o: OrderType
    S: OrderSide
    z: str
    V: OrderSelfTradePrevention


class WebSocketResponseOrderShort(_WebSocketResponseOrderShortRequiredAttribs, total=False):
    """
    Attributes:
        m: (market) Market symbol
        i: (orderId) Exchange-assigned order identifier
        c: (clientOrderId) Client-specified order identifier
        w : (wallet) Ethereum address of placing wallet
        t: (executionTime) Timestamp of the most recent update
        T: (time) Timestamp of initial order processing by the matching engine
        x: (update) Type of order update, see values
        X: (status) Order status, see values
        u: (sequence) order book update sequence number, only included if update type triggers an
            order book update
        o: (type) Order type, see values
        S: (side) Order side, buy or sell
        q: (originalQuantity) Original quantity specified by the order in base terms, omitted for
            market orders specified in quote terms
        Q: (originalQuoteQuantity) Original quantity specified by the order in quote terms, only
            present for market orders specified in quote term
        z: (executedQuantity) Quantity that has been executed in base terms
        Z: (cumulativeQuoteQuantity) Cumulative quantity that has been spent (buy orders) or
            received (sell orders) in quote terms, omitted if unavailable for historical orders
        v: (avgExecutionPrice) Weighted average price of fills associated with the order; only
            present with fills
        p: (price) Original price specified by the order in quote terms, omitted for all market
            orders
        P: (stopPrice) Stop loss or take profit price, only present for stopLoss, stopLossLimit,
            takeProfit, and takeProfitLimit orders
        f: (timeInForce) Time in force policy, see values, only present for limit orders
        V: (selfTradePrevention) Self-trade prevention policy, see values
        F: (fills) Array of order fill objects
    """

    c: str
    u: int
    q: str
    Q: str
    Z: str
    v: str
    p: str
    P: str
    f: OrderTimeInForce
    F: List[WebSocketResponseOrderFillShort]


class _WebSocketResponseOrderLongRequiredAttribs(TypedDict):
    market: str  # m
    orderId: str  # i
    wallet: str  # w
    executionTime: int  # t
    time: int  # T
    update: OrderStateChange  # x
    status: OrderStatus  # X
    type: OrderType  # o
    side: OrderSide  # S
    executedQuantity: str  # z
    selfTradePrevention: OrderSelfTradePrevention  # V


class WebSocketResponseOrderLong(_WebSocketResponseOrderLongRequiredAttribs):
    """
    Attributes:
        market: Market symbol
        orderId: Exchange-assigned order identifier
        clientOrderId: Client-specified order identifier
        wallet: Ethereum address of placing wallet
        executionTime: Timestamp of the most recent update
        time: Timestamp of initial order processing by the matching engine
        update: Type of order update, see values
        status: Order status, see values
        sequence: order book update sequence number, only included if update type triggers
            an order book update
        type: Order type, see values
        side: Order side, buy or sell
        originalQuantity: Original quantity specified by the order in base terms, omitted for
            market orders specified in quote terms
        originalQuoteQuantity: Original quantity specified by the order in quote terms, only
            present for market orders specified in quote terms
        executedQuantity: Quantity that has been executed in base terms
        cumulativeQuoteQuantity: Cumulative quantity that has been spent (buy orders) or received
            (sell orders) in quote terms, omitted if unavailable for historical orders
        avgExecutionPrice: Weighted average price of fills associated with the order; only present
            with fills
        price: Original price specified by the order in quote terms, omitted for all market orders
        stopPrice: Stop loss or take profit price, only present for stopLoss, stopLossLimit,
            takeProfit, and takeProfitLimit orders
        timeInForce: Time in force policy, see values, only present for limit orders
        selfTradePrevention: Self-trade prevention policy, see values
        fills: Array of order fill objects
    """

    clientOrderId: str  # c
    sequence: int  # u
    originalQuantity: str  # q
    originalQuoteQuantity: str  # Q
    cumulativeQuoteQuantity: str  # Z
    avgExecutionPrice: str  # v
    price: str  # p
    stopPrice: str  # P
    timeInForce: OrderTimeInForce  # f
    fills: List[rest_response.RestResponseOrderFill]  # F


class WebSocketResponseTokenPriceShort(TypedDict):
    """
    Attributes:
        t: (token) Token symbol
        p: (price) Current price of token relative to the native asset
    """

    t: str
    p: Optional[str]


class WebSocketResponseTokenPriceLong(TypedDict):
    """
    Attributes:
        token: Token symbol
        price: Current price of token relative to the native asset
    """

    token: str
    price: Optional[str]


class WebSocketResponseTickerSubscriptionMessageShort(TypedDict):
    type: Literal["tickers"]
    data: WebSocketResponseTickerShort


class WebSocketResponseTradeSubscriptionMessageShort(TypedDict):
    type: Literal["trades"]
    data: WebSocketResponseTradeShort


class WebSocketResponseCandleSubscriptionMessageShort(TypedDict):
    type: Literal["candles"]
    data: WebSocketResponseCandleShort


class WebSocketResponseL1OrderBookSubscriptionMessageShort(TypedDict):
    type: Literal["l1orderbook"]
    data: WebSocketResponseL1OrderBookShort


class WebSocketResponseL2OrderBookSubscriptionMessageShort(TypedDict):
    type: Literal["l2orderbook"]
    data: WebSocketResponseL2OrderBookShort


class WebSocketResponseBalanceSubscriptionMessageShort(TypedDict):
    type: Literal["balances"]
    data: WebSocketResponseBalanceShort


class WebSocketResponseOrderSubscriptionMessageShort(TypedDict):
    type: Literal["orders"]
    data: WebSocketResponseOrderShort


class WebSocketResponseTokenPriceSubscriptionMessageShort(TypedDict):
    type: Literal["tokenprice"]
    data: WebSocketResponseTokenPriceShort


# Short-hand response payloads
WebSocketResponseSubscriptionMessageShort = Union[
    WebSocketResponseTickerSubscriptionMessageShort,
    WebSocketResponseTradeSubscriptionMessageShort,
    WebSocketResponseCandleSubscriptionMessageShort,
    WebSocketResponseL1OrderBookSubscriptionMessageShort,
    WebSocketResponseL2OrderBookSubscriptionMessageShort,
    WebSocketResponseBalanceSubscriptionMessageShort,
    WebSocketResponseOrderSubscriptionMessageShort,
    WebSocketResponseTokenPriceSubscriptionMessageShort,
]


class WebSocketResponseTickerSubscriptionMessageLong(TypedDict):
    type: Literal["tickers"]
    data: WebSocketResponseTickerLong


class WebSocketResponseTradeSubscriptionMessageLong(TypedDict):
    type: Literal["trades"]
    data: WebSocketResponseTradeLong


class WebSocketResponseCandleSubscriptionMessageLong(TypedDict):
    type: Literal["candles"]
    data: WebSocketResponseCandleLong


class WebSocketResponseL1OrderBookSubscriptionMessageLong(TypedDict):
    type: Literal["l1orderbook"]
    data: WebSocketResponseL1OrderBookLong


class WebSocketResponseL2OrderBookSubscriptionMessageLong(TypedDict):
    type: Literal["l2orderbook"]
    data: WebSocketResponseL2OrderBookLong


class WebSocketResponseBalanceSubscriptionMessageLong(TypedDict):
    type: Literal["balances"]
    data: WebSocketResponseBalanceLong


class WebSocketResponseOrderSubscriptionMessageLong(TypedDict):
    type: Literal["orders"]
    data: WebSocketResponseOrderLong


class WebSocketResponseTokenPriceSubscriptionMessageLong(TypedDict):
    type: Literal["tokenprice"]
    data: WebSocketResponseTokenPriceLong


# Transformer (long-form) response payloads
WebSocketResponseSubscriptionMessageLong = Union[
    WebSocketResponseTickerSubscriptionMessageLong,
    WebSocketResponseTradeSubscriptionMessageLong,
    WebSocketResponseCandleSubscriptionMessageLong,
    WebSocketResponseL1OrderBookSubscriptionMessageLong,
    WebSocketResponseL2OrderBookSubscriptionMessageLong,
    WebSocketResponseBalanceSubscriptionMessageLong,
    WebSocketResponseOrderSubscriptionMessageLong,
    WebSocketResponseTokenPriceSubscriptionMessageLong,
]


class WebSocketResponseErrorData(TypedDict):
    code: str
    message: str


class _WebSocketResponseErrorRequiredAttribs(TypedDict):
    type: Literal["error"]
    data: WebSocketResponseErrorData


class WebSocketResponseError(_WebSocketResponseErrorRequiredAttribs, total=False):
    """
    Error response

    Attributes:
        cid
        error
        data
        data.code: error short code
        data.message: human readable error message
    """

    cid: str


class _WebSocketResponseSubscriptionsRequiredAttribs(TypedDict):
    type: Literal["subscriptions"]
    subscriptions: List[WebSocketRequestSubscription]


class WebSocketResponseSubscriptions(_WebSocketResponseSubscriptionsRequiredAttribs, total=False):
    """
    Subscriptions response

    Attributes:
        cid
        type: subscriptions
        subscriptions
        Subscription.name: subscription name
        Subscription.markets: markets
        Subscription.interval: candle interval
        Subscription.wallet: wallet address
    """

    cid: str


WebSocketResponse = Union[
    WebSocketResponseError, WebSocketResponseSubscriptions, WebSocketResponseSubscriptionMessageLong
]

# Response message without transformation to human readable form
WebSocketResponseRawMessage = WebSocketResponseSubscriptionMessageShort
