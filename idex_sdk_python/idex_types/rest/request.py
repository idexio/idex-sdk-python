from typing import List, Literal, TypedDict, Union

from idex_sdk_python.idex_types.enums import (
    CandleInterval,
    OrderSelfTradePrevention,
    OrderSide,
    OrderTimeInForce,
    OrderType,
)


class RestRequestFindLiquidityPools(TypedDict, total=False):
    """
    Attributes:
        market: Target market
        tokenA: Address of one reserve token
        tokenB: Address of one reserve token
    """

    market: str
    tokenA: str
    tokenB: str


class RestRequestAddLiquidity(TypedDict):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        tokenA: Asset by address
        tokenB: Asset by address
        amountADesired: Maximum amount of tokenA to add to the liquidity pool
        amountBDesired: Maximum amount of tokenB to add to the liquidity pool
        amountAMin: Minimum amount of tokenA to add to the liquidity pool
        amountBMin: Minimum amount of tokenB to add to the liquidity pool
        to: Wallet to credit LP tokens, or the custodian contract address to leave on exchange
    """

    nonce: str
    wallet: str
    tokenA: str
    tokenB: str
    amountADesired: str
    amountBDesired: str
    amountAMin: str
    amountBMin: str
    to: str


class RestRequestRemoveLiquidity(TypedDict):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        tokenA: Asset by address
        tokenB: Asset by address
        liquidity: LP tokens to burn
        amountAMin: Minimum amount of tokenA to add to the liquidity pool
        amountBMin: Minimum amount of tokenB to add to the liquidity pool
        to: Wallet to credit LP tokens, or the custodian contract address to leave on exchange
    """

    nonce: str
    wallet: str
    tokenA: str
    tokenB: str
    liquidity: str
    amountAMin: str
    amountBMin: str
    to: str


class RestRequestFindWithPagination(TypedDict, total=False):
    start: int
    end: int
    limit: int


class _RestRequestFindLiquidityChangeRequiredAttribs(TypedDict):
    nonce: str
    wallet: str


class RestRequestFindLiquidityChange(_RestRequestFindLiquidityChangeRequiredAttribs, total=False):
    initiatingTxId: str


class RestRequestFindLiquidityAddition(
    RestRequestFindLiquidityChange, RestRequestFindWithPagination, total=False
):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        liquidityAdditionId: Single liquidityAdditionId to return; exclusive with initiatingTxId
        initiatingTxId: Transaction id of the Exchange contract addLiquidity or addLiquidityETH
            call transaction, only applies to chain-initiated liquidity additions; exclusive
            with liquidityAdditionId
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Liquidity additions created at the same timestamp or after fromId
    """

    liquidityAdditionId: str
    fromId: str


class RestRequestFindLiquidityRemoval(
    RestRequestFindLiquidityChange, RestRequestFindWithPagination, total=False
):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        liquidityRemovalId: Single liquidityRemovalId to return; exclusive with initiatingTxId
        initiatingTxId: Transaction id of the Exchange contract removeLiquidity or
            removeLiquidityETH call transaction, only applies to chain-initiated liquidity
            removals; exclusive with liquidityRemovalId
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Liquidity additions created at the same timestamp or after fromId
    """

    liquidityRemovalId: str
    fromId: str


class _RestRequestFindLiquidityChangesRequiredAttribs(RestRequestFindWithPagination):
    nonce: str
    wallet: str


class RestRequestFindLiquidityChanges(_RestRequestFindLiquidityChangesRequiredAttribs, total=False):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Deposits created at the same timestamp or after fromId
    """

    fromId: str


class RestRequestCancelOrdersBase(TypedDict):
    nonce: str
    wallet: str


class RestRequestCancelOrder(RestRequestCancelOrdersBase):
    orderId: str


class RestRequestCancelOrders(RestRequestCancelOrdersBase, total=False):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        market: Base-quote pair e.g. 'IDEX-ETH'
    """

    market: str


RestRequestCancelOrderOrOrders = Union[RestRequestCancelOrder, RestRequestCancelOrders]


class RestRequestCancelOrdersBody(TypedDict):
    parameters: RestRequestCancelOrderOrOrders
    signature: str


class RestRequestFindByWallet(TypedDict):
    nonce: str
    wallet: str


class RestRequestFindBalances(RestRequestFindByWallet, total=False):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        assets: Asset symbols
    """

    assets: List[str]


class RestRequestFindCandles(RestRequestFindWithPagination):
    """
    Attributes:
        market: Base-quote pair e.g. 'IDEX-ETH'
        interval: Time interval for data
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
    """

    market: str
    interval: CandleInterval


class RestRequestFindDeposit(RestRequestFindByWallet):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        depositId
    """

    depositId: str


class RestRequestFindDeposits(RestRequestFindByWallet, RestRequestFindWithPagination, total=False):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        asset: Asset by symbol
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Deposits created at the same timestamp or after fromId
    """

    asset: str
    fromId: str


class RestRequestFindFill(RestRequestFindByWallet):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        fillId
    """

    fillId: str


class RestRequestFindFills(RestRequestFindByWallet, RestRequestFindWithPagination, total=False):
    """
    Attributes:
        nonce: UUIDv1
        wallet: Ethereum wallet address
        market: Base-quote pair e.g. 'IDEX-ETH'
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Fills created at the same timestamp or after fillId
    """

    market: str
    fromId: str


class RestRequestFindMarkets(TypedDict, total=False):
    """
    Attributes:
        market: Target market, all markets are returned if omitted
    """

    market: str


class RestRequestFindOrder(RestRequestFindByWallet):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        orderId: Single orderId or clientOrderId to cancel; prefix client-provided ids with client
    """

    orderId: str


class RestRequestFindOrders(RestRequestFindByWallet, RestRequestFindWithPagination, total=False):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        market: Base-quote pair e.g. 'IDEX-ETH'
        closed: false only returns active orders on the order book; true only returns orders that
            are no longer on the order book and resulted in at least one fill; only applies if
            orderId is absent
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: order_id of the earliest (oldest) order, only applies if orderId is absent
    """

    market: str
    closed: bool
    fromId: str


class RestRequestFindTrades(RestRequestFindWithPagination, total=False):
    """
    Attributes:
        market: Base-quote pair e.g. 'IDEX-ETH'
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Trades created at the same timestamp or after from_id
    """

    market: str
    fromId: str


class RestRequestFindWithdrawal(RestRequestFindByWallet):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        withdrawalId
    """

    withdrawalId: str


class RestRequestFindWithdrawals(
    RestRequestFindByWallet, RestRequestFindWithPagination, total=False
):
    """
    Attributes:
        nonce: UUIDv1
        wallet
        asset: Asset by symbol
        assetContractAddress: Asset by contract address
        start: Starting timestamp (inclusive)
        end: Ending timestamp (inclusive)
        limit: Max results to return from 1-1000
        fromId: Withdrawals created after the fromId
    """

    asset: str
    assetContractAddress: str
    fromId: str


class _RestRequestAllOrderParametersRequiredAttribs(TypedDict):
    nonce: str
    wallet: str
    market: str
    type: OrderType
    side: OrderSide


class RestRequestAllOrderParameters(_RestRequestAllOrderParametersRequiredAttribs, total=False):
    timeInForce: OrderTimeInForce
    clientOrderId: str
    selfTradePrevention: OrderSelfTradePrevention
    cancelAfter: int


# Limit orders


class RestRequestLimitOrder(RestRequestAllOrderParameters):
    type: Literal["limit", "limitMaker"]  # type: ignore
    price: str


class RestRequestLimitOrderByBaseQuantity(RestRequestLimitOrder):
    quantity: str


class RestRequestLimitOrderByQuoteQuantity(RestRequestLimitOrder):
    quoteOrderQuantity: str


# Market orders


class RestRequestMarketOrder(RestRequestAllOrderParameters):
    type: Literal["market"]  # type: ignore


class RestRequestMarketOrderByBaseQuantity(RestRequestMarketOrder):
    quantity: str


class RestRequestMarketOrderByQuoteQuantity(RestRequestMarketOrder):
    quoteOrderQuantity: str


# Stop-loss orders


class RestRequestStopLossOrder(RestRequestAllOrderParameters):
    type: Literal["stopLoss"]  # type: ignore
    stopPrice: str


class RestRequestStopLossOrderByBaseQuantity(RestRequestStopLossOrder):
    quantity: str


class RestRequestStopLossOrderByQuoteQuantity(RestRequestStopLossOrder):
    quoteOrderQuantity: str


# Stop-loss limit orders


class RestRequestStopLossLimitOrder(RestRequestAllOrderParameters):
    type: Literal["stopLossLimit"]  # type: ignore
    price: str
    stopPrice: str


class RestRequestStopLossLimitOrderByBaseQuantity(RestRequestStopLossLimitOrder):
    quantity: str


class RestRequestStopLossLimitOrderByQuoteQuantity(RestRequestStopLossLimitOrder):
    quoteOrderQuantity: str


# Take-profit orders


class RestRequestTakeProfitOrder(RestRequestAllOrderParameters):
    type: Literal["takeProfit"]  # type: ignore
    stopPrice: str


class RestRequestTakeProfitOrderByBaseQuantity(RestRequestTakeProfitOrder):
    quantity: str


class RestRequestTakeProfitOrderByQuoteQuantity(RestRequestTakeProfitOrder):
    quoteOrderQuantity: str


# Take-profit limit orders


class RestRequestTakeProfitLimitOrder(RestRequestAllOrderParameters):
    type: Literal["takeProfitLimit"]  # type: ignore
    price: str
    stopPrice: str


class RestRequestTakeProfitLimitOrderByBaseQuantity(RestRequestTakeProfitLimitOrder):
    quantity: str


class RestRequestTakeProfitLimitOrderByQuoteQuantity(RestRequestTakeProfitLimitOrder):
    quoteOrderQuantity: str


RestRequestOrderByBaseQuantity = Union[
    RestRequestLimitOrderByBaseQuantity,
    RestRequestMarketOrderByBaseQuantity,
    RestRequestStopLossOrderByBaseQuantity,
    RestRequestStopLossLimitOrderByBaseQuantity,
    RestRequestTakeProfitOrderByBaseQuantity,
    RestRequestTakeProfitLimitOrderByBaseQuantity,
]


RestRequestOrderByQuoteQuantity = Union[
    RestRequestLimitOrderByQuoteQuantity,
    RestRequestMarketOrderByQuoteQuantity,
    RestRequestStopLossOrderByQuoteQuantity,
    RestRequestStopLossLimitOrderByQuoteQuantity,
    RestRequestTakeProfitOrderByQuoteQuantity,
    RestRequestTakeProfitLimitOrderByQuoteQuantity,
]


RestRequestOrderWithPrice = Union[
    RestRequestLimitOrder,
    RestRequestStopLossLimitOrder,
    RestRequestTakeProfitLimitOrder,
]


RestRequestOrderWithStopPrice = Union[
    RestRequestStopLossOrder,
    RestRequestStopLossLimitOrder,
    RestRequestTakeProfitLimitOrder,
]


RestRequestOrder = Union[RestRequestOrderByBaseQuantity, RestRequestOrderByQuoteQuantity]


class RestRequestCreateOrderBody(TypedDict):
    parameters: RestRequestOrder
    signature: str


class _RestRequestWithdrawalBaseRequiredAttribs(TypedDict):
    nonce: str
    wallet: str
    quantity: str


class RestRequestWithdrawalBase(_RestRequestWithdrawalBaseRequiredAttribs, total=False):
    # Currently has no effect
    autoDispatchEnabled: bool


class RestRequestWithdrawalBySymbol(RestRequestWithdrawalBase):
    asset: str


class RestRequestWithdrawalByAddress(RestRequestWithdrawalBase):
    assetContractAddress: str


RestRequestWithdrawal = Union[RestRequestWithdrawalBySymbol, RestRequestWithdrawalByAddress]


class RestRequestCreateWithdrawalBody(TypedDict):
    parameters: RestRequestWithdrawal
    signature: str


class RestRequestAssociateWallet(TypedDict):
    """
    Attributes:
        nonce: UUIDv1
        wallet: The wallet to associate with the authenticated account
    """

    nonce: str
    wallet: str
