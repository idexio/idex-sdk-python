from typing import List, Literal, Optional, Tuple, TypedDict

from idex_sdk.idex_types.enums import (
    EthTransactionStatus,
    Liquidity,
    MarketStatus,
    MarketType,
    OrderSelfTradePrevention,
    OrderSide,
    OrderStatus,
    OrderTimeInForce,
    OrderType,
    TradeType,
)


class _RestResponseAssetRequiredAttribs(TypedDict):
    name: str
    symbol: str
    contractAddress: str
    assetDecimals: int
    exchangeDecimals: Literal[8]  # this is hardcoded everywhere and should not be changed


class RestResponseAsset(_RestResponseAssetRequiredAttribs, total=False):
    maticPrice: str


class RestResponseBalance(TypedDict):
    """
    Attributes:
        asset: Asset symbol
        quantity: Total quantity of the asset held by the wallet on the exchange
        availableForTrade: Quantity of the asset available for trading; quantity: locked
        locked: Quantity of the asset held in trades on the order book
        usdValue: Total value of the asset held by the wallet on the exchange in USD
    """

    asset: str
    quantity: str
    availableForTrade: str
    locked: str
    usdValue: Optional[str]


class RestResponseCandle(TypedDict):
    """
    Attributes:
        start: Time of the start of the interval
        open: Price of the first fill of the interval in quote terms
        high: Price of the highest fill of the interval in quote terms
        low: Price of the lowest fill of the interval in quote terms
        close: Price of the last fill of the interval in quote terms
        volume: Total volume of the period in base terms
        sequence: Fill sequence number of the last trade in the interval
    """

    start: int
    open: str
    high: str
    low: str
    close: str
    volume: str
    sequence: int


class RestResponseDeposit(TypedDict):
    """
    Asset deposits into smart contract

    Attributes:
        depositId: IDEX-issued deposit identifier
        asset: Asset by symbol
        quantity: Deposit amount in asset terms
        txId: Ethereum transaction hash
        txTime: Timestamp of the Ethereum deposit transaction
        confirmationTime: Timestamp of credit on IDEX including block confirmations
    """

    depositId: str
    asset: str
    quantity: str
    txId: str
    txTime: int
    confirmationTime: int


class RestResponseExchangeInfo(TypedDict):
    """
    Attributes:
        timeZone: Server time zone, always UTC
        serverTime: Current server time
        maticDepositContractAddress: Polygon address of the exchange smart contract for deposits
        maticCustodyContractAddress: Polygon address of the custody smart contract for certain add
            and remove liquidity calls
        maticUsdPrice: Current price of MATIC in USD
        gasPrice: Current gas price used by the exchange for trade settlement and withdrawal
            transactions in Gwei
        volume24hUsd: Total exchange trading volume for the trailing 24 hours in USD
        totalVolumeUsd: Total exchange trading volume for IDEX v3 on Polygon in USD
        totalTrades: Total number of trade executions for IDEX v3 on Polygon
        totalValueLockedUsd: Total value locked in IDEX v3 on Polygon in USD
        idexTokenAddress: Token contract address for the IDEX token on Polygon
        idexUsdPrice: Current price of the IDEX token in USD
        idexMarketCapUsd: Market capitalization of the IDEX token in USD
        makerFeeRate: Maker trade fee rate
        takerFeeRate: Total taker trade fee rate
        takerIdexFeeRate: Taker trade fee rate collected by IDEX; used in computing synthetic
            price levels for real-time order books
        takerLiquidityProviderFeeRate: Taker trade fee rate collected by liquidity providers; used
            in computing synthetic price levels for real-time order books
        makerTradeMinimum: Minimum size of an order that can rest on the order book in MATIC,
            applies to both MATIC and tokens
        takerTradeMinimum: Minimum order size that is accepted by the matching engine for
            execution in MATIC, applies to both MATIC and tokens
        withdrawMinimum: Minimum withdrawal amount in MATIC, applies to both MATIC and tokens
        liquidityAdditionMinimum: Minimum liquidity addition amount in MATIC, applies to both
            MATIC and tokens
        liquidityRemovalMinimum: Minimum withdrawal amount in MATIC, applies to both
            MATIC and tokens
        blockConfirmationDelay: Minimum number of block confirmations before on-chain transactions
            are processed
    """

    timeZone: str
    serverTime: int
    maticDepositContractAddress: str
    maticCustodyContractAddress: str
    maticUsdPrice: str
    gasPrice: int
    volume_24HUsd: str
    totalVolumeUsd: str
    totalTrades: int
    totalValueLockedUsd: str
    idexStakingValueLockedUsd: str
    idexTokenAddress: str
    idexUsdPrice: str
    idexMarketCapUsd: str
    makerFeeRate: str
    takerFeeRate: str
    takerIdexFeeRate: str
    takerLiquidityProviderFeeRate: str
    makerTradeMinimum: str
    takerTradeMinimum: str
    withdrawMinimum: str
    liquidityAdditionMinimum: str
    liquidityRemovalMinimum: str
    blockConfirmationDelay: int


class _RestResponseOrderFillRequiredAttribs(TypedDict):
    fillId: str
    price: str
    quantity: str
    quoteQuantity: str
    time: int
    makerSide: OrderSide
    sequence: int
    fee: str
    feeAsset: str
    liquidity: Liquidity
    type: TradeType
    txId: Optional[str]
    txStatus: EthTransactionStatus


class RestResponseOrderFill(_RestResponseOrderFillRequiredAttribs, total=False):
    """
    Attributes:
        fillId: Internal ID of fill
        price: Executed price of fill in quote terms
        quantity: Executed quantity of fill in base terms
        quoteQuantity: Executed quantity of trade in quote terms
        orderBookQuantity: Quantity of the fill in base terms supplied by order book liquidity,
            omitted for pool fills
        orderBookQuoteQuantity: Quantity of the fill in quote terms supplied by order book
            liquidity, omitted for pool fills
        poolQuantity: Quantity of the fill in base terms supplied by pool liquidity, omitted for
            orderBook fills
        poolQuoteQuantity: Quantity of the fill in quote terms supplied by pool liquidity, omitted
            for orderBook fills
        time: Fill timestamp
        makerSide: Which side of the order the liquidity maker was on
        sequence: Last trade sequence number for the market
        fee: Fee amount on fill
        feeAsset: Which token the fee was taken in
        gas
        liquidity
        type: orderBook, pool, or hybrid
        txId: Ethereum transaction ID, if available
        txStatus: Ethereum transaction status
    """

    orderBookQuantity: str
    orderBookQuoteQuantity: str
    poolQuantity: str
    poolQuoteQuantity: str
    gas: str


class _RestResponseFillRequiredAttribs(RestResponseOrderFill):
    orderId: str
    market: str
    side: OrderSide


class RestResponseFill(_RestResponseFillRequiredAttribs, total=False):
    """
    Attributes:
        fillId: Internal ID of fill
        price: Executed price of fill in quote terms
        quantity: Executed quantity of fill in base terms
        quoteQuantity: Executed quantity of fill in quote terms
        orderBookQuantity: Quantity of the fill in base terms supplied by order book liquidity,
            omitted for pool fills
        orderBookQuoteQuantity: Quantity of the fill in quote terms supplied by order book
            liquidity, omitted for pool fills
        poolQuantity: Quantity of the fill in base terms supplied by pool liquidity, omitted for
            orderBook fills
        poolQuoteQuantity: Quantity of the fill in quote terms supplied by pool liquidity, omitted
            for orderBook fills
        time: Fill timestamp
        makerSide: Which side of the order the liquidity maker was on
        sequence: Last trade sequence number for the market
        market: Base-quote pair e.g. 'IDEX-ETH'
        orderId: Internal ID of order
        clientOrderId: Client-provided ID of order
        side: Orders side, buy or sell
        fee: Fee amount on fill
        feeAsset: Which token the fee was taken in
        gas: Amount collected to cover trade settlement gas costs, only present for taker
        liquidity: Whether the fill is the maker or taker in the trade from the perspective of the
            requesting API account, maker or taker
        type: Fill type
        txId: Ethereum transaction ID, if available
        txStatus: Ethereum transaction status
    """

    clientOrderId: str


class RestResponseLiquidityPool(TypedDict):
    """
    Attributes:
        tokenA: Address of one reserve token
        tokenB: Address of one reserve token
        reserveA: Quantity of token A held as reserve in token precision, not pips
        reserveB: Quantity of token B held as reserve in token precision, not pips
        liquidityToken: Address of the liquidity provider (LP) token
        totalLiquidity: Total quantity of liquidity provider (LP) tokens minted in token
            precision, not pips
        reserveUsd: Total value of reserves in USD
        market: Market symbol of pool's associated hybrid market
    """

    tokenA: str
    tokenB: str
    reserveA: str
    reserveB: str
    liquidityToken: str
    totalLiquidity: str
    reserveUsd: str
    market: str


class _RestResponseLiquidityBaseRequiredAttribs(TypedDict):
    tokenA: str
    tokenB: str
    amountA: Optional[str]
    amountB: Optional[str]
    liquidity: Optional[str]
    time: int
    initiatingTxId: Optional[str]
    feeTokenA: Optional[str]
    feeTokenB: Optional[str]
    txId: Optional[str]
    txStatus: Optional[EthTransactionStatus]


class RestResponseLiquidityBase(_RestResponseLiquidityBaseRequiredAttribs, total=False):
    errorCode: str
    errorMessage: str


class RestResponseLiquidityAddition(RestResponseLiquidityBase):
    """
    Attributes:
        liquidityAdditionId: Internal ID of liquidity addition
        tokenA: Asset symbol
        tokenB: Asset symbol
        amountA: Amount of tokenA added to the liquidity pool
        amountB: Amount of tokenB added to the liquidity pool
        liquidity: Amount of liquidity provided (LP) tokens minted
        time: Liquidity addition timestamp
        initiatingTxId: On chain initiated transaction ID, if available
        errorCode: Error short code present on liquidity addition error
        errorMessage: Human-readable error message present on liquidity addition error
        feeTokenA: Amount of tokenA collected as fees
        feeTokenB: Amount of tokenB collected as fees
        txId: Ethereum transaction ID, if available
        txStatus: Ethereum transaction status
    """

    liquidityAdditionId: Optional[str]


class RestResponseLiquidityPoolReserves(TypedDict):
    """
    Attributes:
        baseReserveQuantity: reserve quantity of base asset in pool
        quoteReserveQuantity: reserve quantity of quote asset in pool
    """

    baseReserveQuantity: str
    quoteReserveQuantity: str


class RestResponseLiquidityRemoval(RestResponseLiquidityBase):
    """
    Attributes:
        liquidityRemovalId: Internal ID of liquidity removal
        tokenA: Asset symbol
        tokenB: Asset symbol
        amountA: Amount of tokenA added to the liquidity pool
        amountB: Amount of tokenB added to the liquidity pool
        liquidity: Amount of liquidity provided (LP) tokens minted
        time: Liquidity addition timestamp
        initiatingTxId: On chain initiated transaction ID, if available
        errorCode: Error short code present on liquidity addition error
        errorMessage: Human-readable error message present on liquidity addition error
        feeTokenA: Amount of tokenA collected as fees
        feeTokenB: Amount of tokenB collected as fees
        txId: Ethereum transaction ID, if available
        txStatus: Ethereum transaction status
    """

    liquidityRemovalId: Optional[str]


class RestResponseMarket(TypedDict):
    """
    Attributes:
        market: Market symbol
        type: Market type
        status: Market trading status
        baseAsset: Base asset symbol
        baseAssetPrecision: Exchange decimal precision of the base asset, always 8 due to
            precision normalization
        quoteAsset: Quote asset symbol
        quoteAssetPrecision: Exchange decimal precision of the base asset, always 8 due to
            precision normalization
        makerFeeRate: Maker trade fee rate
        takerFeeRate: Total taker trade fee rate
        takerIdexFeeRate: Taker trade fee rate collected by IDEX; used in computing synthetic
            price levels for real-time order books
        takerLiquidityProviderFeeRate: Taker trade fee rate collected by liquidity providers; used
            in computing synthetic price levels for real-time order books
        tickSize: Market tick size (minimum change in order price)
    """

    market: str
    type: MarketType
    status: MarketStatus
    baseAsset: str
    baseAssetPrecision: int
    quoteAsset: str
    quoteAssetPrecision: int
    makerFeeRate: str
    takerFeeRate: str
    takerIdexFeeRate: str
    takerLiquidityProviderFeeRate: str
    tickSize: str


class _RestResponseOrderRequiredAttribs(TypedDict):
    market: str
    orderId: str
    wallet: str
    time: int
    status: OrderStatus
    type: OrderType
    side: OrderSide
    executedQuantity: str
    selfTradePrevention: OrderSelfTradePrevention


class RestResponseOrder(_RestResponseOrderRequiredAttribs, total=False):
    """
    Attributes:
        market: Market symbol as base-quote pair e.g. 'IDEX-ETH'
        orderId: Exchange-assigned order identifier
        clientOrderId: Client-specified order identifier
        wallet: Ethereum address of placing wallet
        time: Time of initial order processing by the matching engine
        status: Current order status
        errorCode: Error short code explaining order error or failed batch cancel
        errorMessage: Error description explaining order error or failed batch cancel
        type: Order type
        side: Order side
        originalQuantity: Original quantity specified by the order in base terms, omitted for
            market orders specified in quote terms
        originalQuoteQuantity: Original quantity specified by the order in quote terms, only
            present for market orders specified in quote terms
        executedQuantity: Quantity that has been executed in base terms
        cumulativeQuoteQuantity: Cumulative quantity that has been spent (buy orders) or received
            (sell orders) in quote terms, omitted if unavailable for historical orders
        avgExecutionPrice: Weighted average price of fills associated with the order; only present
            with fills
        price -	Original price specified by the order in quote terms, omitted for all market orders
        stopPrice: Stop loss or take profit price, only present for stopLoss, stopLossLimit,
            takeProfit, and takeProfitLimit orders
        timeInForce: Time in force policy, see values, only present for limit orders
        selfTradePrevention: Self-trade prevention policy, see values
        fills: Array of order fill objects
    """

    clientOrderId: str
    errorCode: str
    errorMessage: str
    originalQuantity: str
    originalQuoteQuantity: str
    cumulativeQuoteQuantity: str
    avgExecutionPrice: str
    price: str
    stopPrice: str
    timeInForce: OrderTimeInForce
    fills: List[RestResponseOrderFill]


class RestResponseCanceledOrder(TypedDict):
    orderId: str


# price and size as decimal strings
# numorders is the number of limit orders at this price level (0 for synthetic levels)
Price = str
Size = str
NumOrders = int
RestResponseOrderBookPriceLevel = Tuple[Price, Size, NumOrders]


class RestResponseOrderBook(TypedDict):
    sequence: int
    bids: List[RestResponseOrderBookPriceLevel]
    asks: List[RestResponseOrderBookPriceLevel]
    pool: Optional[RestResponseLiquidityPoolReserves]


class RestResponseTicker(TypedDict):
    """
    Attributes:
        market: Base-quote pair e.g. 'IDEX-ETH'
        time: Time when data was calculated, open and change is assumed to be trailing 24h
        open: Price of the first trade for the period in quote terms
        high: Highest traded price in the period in quote terms
        low: Lowest traded price in the period in quote terms
        close: Same as last
        closeQuantity: Quantity of the last period in base terms
        baseVolume: 24h volume in base terms
        quoteVolume: 24h volume in quote terms
        percentChange: % change from open to close
        numTrades: Number of fills for the market in the period
        ask: Best ask price on the order book
        bid: Best bid price on the order book
        sequence: Last trade sequence number for the market
    """

    market: str
    time: int
    open: Optional[str]
    high: Optional[str]
    low: Optional[str]
    close: Optional[str]
    closeQuantity: Optional[str]
    baseVolume: str
    quoteVolume: str
    percentChange: str
    numTrades: int
    ask: Optional[str]
    bid: Optional[str]
    sequence: Optional[int]


class RestResponseTrade(TypedDict):
    """
    Attributes:
        fillId: Internal ID of fill
        price: Executed price of trade in quote terms
        quantity: Executed quantity of trade in base terms
        quoteQuantity: Executed quantity of trade in quote terms
        time: Fill timestamp
        makerSide: Which side of the order the liquidity maker was on
        type: orderBook, pool, or hybrid
        sequence: Last trade sequence number for the market
    """

    fillId: str
    price: str
    quantity: str
    quoteQuantity: str
    time: int
    makerSide: OrderSide
    type: TradeType
    sequence: int


class RestResponseUser(TypedDict):
    """
    Attributes:
        depositEnabled: Deposits are enabled for the user account
        orderEnabled: Placing orders is enabled for the user account
        cancelEnabled: Cancelling orders is enabled for the user account
        withdrawEnabled: Withdrawals are enabled for the user account
        totalPortfolioValueUsd: Total value of all holdings deposited on the exchange,
            for all wallets associated with the user account, in USD
        makerFeeRate: User-specific maker trade fee rate
        takerFeeRate: User-specific taker trade fee rate
        takerIdexFeeRate: User-specific liquidity pool taker IDEX fee rate
        takerLiquidityProviderFeeRate: User-specific liquidity pool taker LP provider fee rate
    """

    depositEnabled: bool
    orderEnabled: bool
    cancelEnabled: bool
    withdrawEnabled: bool
    totalPortfolioValueUsd: str
    makerFeeRate: str
    takerFeeRate: str
    takerIdexFeeRate: str
    takerLiquidityProviderFeeRate: str


class RestResponseWallet(TypedDict):
    """
    Attributes:
        address: Ethereum address of the wallet
        totalPortfolioValueUsd: Total value of all holdings deposited on the exchange for the
            wallet in USD
        time: Timestamp of association of the wallet with the user account
    """

    address: str
    totalPortfolioValueUsd: str
    time: int


class RestResponseWithdrawalBase(TypedDict):
    withdrawalId: str
    quantity: str
    time: int
    fee: str
    txId: Optional[str]
    txStatus: EthTransactionStatus


class RestResponseWithdrawal(RestResponseWithdrawalBase):
    """
    Attributes:
        withdrawalId: Exchange-assigned withdrawal identifier
        asset: Symbol of the withdrawn asset, exclusive with assetContractAddress
        assetContractAddress]: Token contract address of withdrawn asset, exclusive with asset
        quantity: Quantity of the withdrawal
        time: Timestamp of withdrawal API request
        fee: Amount deducted from withdrawal to cover IDEX-paid gas
        txId: Ethereum transaction ID, if available
        txStatus: Ethereum transaction status
    """

    asset: str
    assetContractAddress: str


class RestResponseAssociateWallet(TypedDict):
    """
    Attributes:
        address: Ethereum address of the wallet
        totalPortfolioValueUsd: Total value of all holdings deposited on the exchange for the
            wallet in USD
        time: Timestamp of association of the wallet with the user account
    """

    address: str
    totalPortfolioValueUsd: str
    time: int
