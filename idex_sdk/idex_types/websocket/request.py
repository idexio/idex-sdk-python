from typing import List, Literal, Sequence, TypedDict, Union

from idex_sdk.idex_types.enums import CandleInterval


class WebSocketRequestTickersSubscription(TypedDict):
    """
    Tickers subscription

    Attributes:
        name: 'tickers'
        markets: array of market symbols
    """

    name: Literal["tickers"]
    markets: List[str]


class WebSocketRequestCandlesSubscription(TypedDict):
    """
    Candles subscription

    Attributes:
        name: 'candles'
        markets: array of market symbols
        interval: candle interval
    """

    name: Literal["candles"]
    markets: List[str]
    interval: CandleInterval


class WebSocketRequestTokenPriceSubscription(TypedDict):
    """
    Token price subscription

    Attributes:
        name: 'tokenprice'
        markets: array of market symbols
    """

    name: Literal["tokenprice"]
    markets: List[str]


class WebSocketRequestTradesSubscription(TypedDict):
    """
    Trades subscription

    Attributes:
        name: 'trades'
        markets: array of market symbols
    """

    name: Literal["trades"]
    markets: List[str]


class WebSocketRequestL1OrderBookSubscription(TypedDict):
    """
    L1 order book subscription

    Attributes:
        name: 'l1orderbook'
        markets: array of market symbols
    """

    name: Literal["l1orderbook"]
    markets: List[str]


class WebSocketRequestL2OrderBookSubscription(TypedDict):
    """
    L2 order book subscription

    Attributes:
        name: 'l2orderbook'
        markets: array of market symbols
    """

    name: Literal["l2orderbook"]
    markets: List[str]


class _WebSocketRequestBalancesSubscriptionRequiredAttribs(TypedDict):
    name: Literal["balances"]


class WebSocketRequestBalancesSubscription(
    _WebSocketRequestBalancesSubscriptionRequiredAttribs, total=False
):
    wallet: str


class _WebSocketRequestOrdersSubscriptionRequiredAttribs(TypedDict):
    name: Literal["orders"]


class WebSocketRequestOrdersSubscription(
    _WebSocketRequestOrdersSubscriptionRequiredAttribs, total=False
):
    wallet: str


class WebSocketRequestAuthenticatedSubscriptionNameOnly(TypedDict):
    name: Literal[
        "balances",
        "orders",
    ]


class WebSocketRequestUnauthenticatedSubscriptionNameOnly(TypedDict):
    name: Literal[
        "candles",
        "l1orderbook",
        "l2orderbook",
        "tickers",
        "tokenprice",
        "trades",
    ]


class WebSocketRequestWallet(TypedDict):
    """
    wallet is required and is only handled by the idex-sdk.
    It is used to auto generate the required wsToken
    """

    wallet: str


class AuthTokenWebSocketRequestBalancesSubscription(TypedDict):
    name: Literal["balances"]
    wallet: str


class AuthTokenWebSocketRequestOrdersSubscription(TypedDict):
    name: Literal["orders"]
    wallet: str


WebSocketRequestAuthenticatedSubscription = Union[
    WebSocketRequestBalancesSubscription, WebSocketRequestOrdersSubscription
]


WebSocketRequestUnauthenticatedSubscription = Union[
    WebSocketRequestCandlesSubscription,
    WebSocketRequestL1OrderBookSubscription,
    WebSocketRequestL2OrderBookSubscription,
    WebSocketRequestTickersSubscription,
    WebSocketRequestTokenPriceSubscription,
    WebSocketRequestTradesSubscription,
]

AuthTokenWebSocketRequestAuthenticatedSubscription = Union[
    AuthTokenWebSocketRequestBalancesSubscription, AuthTokenWebSocketRequestOrdersSubscription
]

WebSocketRequestSubscription = Union[
    AuthTokenWebSocketRequestAuthenticatedSubscription, WebSocketRequestUnauthenticatedSubscription
]

AuthTokenWebSocketRequestSubscription = WebSocketRequestSubscription


WebSocketRequestSubscribeShortNames = Literal[
    "balances",
    "candles",
    "orders",
    "l1orderbook",
    "l2orderbook",
    "tickers",
    "tokenprice",
    "trades",
]


WebSocketRequestUnsubscribeShortNames = Literal[
    "balances",
    "orders",
    "candles",
    "l1orderbook",
    "l2orderbook",
    "tickers",
    "tokenprice",
    "trades",
]


class _WebSocketRequestSubscribeRequiredAttribs(TypedDict):
    method: Literal["subscribe"]
    subscriptions: Sequence[
        Union[
            WebSocketRequestUnauthenticatedSubscription,
            WebSocketRequestAuthenticatedSubscription,
            AuthTokenWebSocketRequestAuthenticatedSubscription,
            WebSocketRequestUnauthenticatedSubscriptionNameOnly,
        ]
    ]


# less strict subscribe shape
class WebSocketRequestSubscribe(_WebSocketRequestSubscribeRequiredAttribs, total=False):
    cid: str
    token: str
    markets: List[str]


WebSocketRequestUnsubscribeSubscription = Union[
    WebSocketRequestAuthenticatedSubscriptionNameOnly,
    WebSocketRequestUnauthenticatedSubscriptionNameOnly,
]


class _WebSocketRequestUnsubscribeRequiredAttribs(TypedDict):
    method: Literal["unsubscribe"]


class WebSocketRequestUnsubscribe(_WebSocketRequestUnsubscribeRequiredAttribs, total=False):
    cid: str
    markets: List[str]
    subscriptions: Sequence[
        Union[
            WebSocketRequestUnsubscribeSubscription,
            WebSocketRequestUnsubscribeShortNames,
        ]
    ]


class _WebSocketRequestSubscriptionsRequiredAttribs(TypedDict):
    method: Literal["subscriptions"]


class WebSocketRequestSubscriptions(_WebSocketRequestSubscriptionsRequiredAttribs, total=False):
    cid: str


WebSocketRequest = Union[
    WebSocketRequestSubscribe, WebSocketRequestSubscriptions, WebSocketRequestUnsubscribe
]
