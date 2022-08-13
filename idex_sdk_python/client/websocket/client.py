import asyncio
import json
from typing import (
    Any,
    Callable,
    Coroutine,
    List,
    Optional,
    Sequence,
    Set,
    TypedDict,
    Union,
    cast,
)
from uuid import uuid1

from websockets.client import WebSocketClientProtocol
from websockets.client import connect as ws_connect
from websockets.exceptions import ConnectionClosed

from idex_sdk_python.client.rest.authenticated import RestAuthenticatedClient
from idex_sdk_python.client.utils import derive_base_url
from idex_sdk_python.client.websocket.transform import (
    transform_websocket_short_response_mesg,
)
from idex_sdk_python.client.websocket.utils import remove_wallet_from_sdk_subscription
from idex_sdk_python.idex_types.enums import MultiverseChain
from idex_sdk_python.idex_types.websocket.guards import (
    is_websocket_authenticated_subscription,
)
from idex_sdk_python.idex_types.websocket.request import (
    AuthTokenWebSocketRequestAuthenticatedSubscription,
    WebSocketRequest,
    WebSocketRequestAuthenticatedSubscription,
    WebSocketRequestSubscribe,
    WebSocketRequestSubscription,
    WebSocketRequestSubscriptions,
    WebSocketRequestUnauthenticatedSubscription,
    WebSocketRequestUnauthenticatedSubscriptionNameOnly,
    WebSocketRequestUnsubscribe,
    WebSocketRequestUnsubscribeShortNames,
    WebSocketRequestUnsubscribeSubscription,
)
from idex_sdk_python.idex_types.websocket.response import WebSocketResponse

WebSocketListenerConnect = Callable[[], Coroutine[Any, Any, Any]]
WebSocketListenerDisconnect = Callable[[int, str], Coroutine[Any, Any, Any]]
WebSocketListenerError = Callable[[Exception], Coroutine[Any, Any, Any]]
WebSocketListenerResponse = Callable[[WebSocketResponse], Coroutine[Any, Any, Any]]


# custom ping timeout in ms - how often do we ping the server
# to check for liveness?
PING_TIMEOUT = 30000


class WebSocketClientState(TypedDict):
    # Set to true when the reconnect logic should not be run.
    do_not_reconnect: bool
    is_reconnecting: bool
    # Used to track the number of reconnect attempts for exponential backoff
    reconnect_attempt: int
    connect_timeout: int
    # When the ping timeout is scheduled, it saves its id to this property
    ping_timeout_id: Union[None, int]
    connect_listeners: Set[WebSocketListenerConnect]
    disconnect_listeners: Set[WebSocketListenerDisconnect]
    error_listeners: Set[WebSocketListenerError]
    response_listeners: Set[WebSocketListenerResponse]
    have_ever_started: bool
    background_tasks: Set[asyncio.Task]


class WebSocketClient:
    """
    WebSocket API client

    When apiKey and apiSecret are provided, the client will automatically handle
    WebSocket authentication token generation and refresh. Omit when using only public
    WebSocket subscriptions.
    """

    state: WebSocketClientState = {
        "do_not_reconnect": False,
        "is_reconnecting": False,
        "reconnect_attempt": 0,
        "connect_timeout": 5000,
        "ping_timeout_id": None,
        "connect_listeners": set(),
        "disconnect_listeners": set(),
        "error_listeners": set(),
        "response_listeners": set(),
        "have_ever_started": False,
        "background_tasks": set(),
    }

    base_url: str
    should_reconnect_automatically: bool
    connect_timeout: int
    websocket_auth_token_fetch: Optional[Callable[[str], str]]
    ws: Optional[WebSocketClientProtocol] = None

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        should_reconnect_automatically: bool = False,
        connect_timeout: Optional[int] = None,
        sandbox: bool = False,
        multiverse_chain: MultiverseChain = MultiverseChain.MATIC,
        base_url: Optional[str] = None,
        websocket_auth_token_fetch: Optional[Callable[[str], str]] = None,
    ):
        """
        Args:
            api_key: Used to authenticate user when automatically refreshing WS token
            api_secret: Used to compute HMAC signature when automatically refreshing WS token
                receiving push updates. Eg. {market}@{subscription}_{option}
            should_reconnect_automatically: If true, automatically reconnects when connection is
                closed by the server or network errors
            connect_timeout: Timeout (in milliseconds) before failing when trying to connect to
                the WebSocket. Defaults to 5000.
            sandbox: If true, client will point to API sandbox
            multiverse_chain: Which multiverse chain the client will point to
        """
        base_url = derive_base_url(
            api_type="websocket",
            multiverse_chain=multiverse_chain,
            sandbox=sandbox,
            override_base_url=base_url,
        )

        if (api_key or api_secret) and websocket_auth_token_fetch:
            raise Exception(
                "Invalid configuration, cannot specify both API credentials and "
                "websocket_auth_token_fetch"
            )
        if (api_key and not api_secret) or (not api_key and api_secret):
            raise Exception(
                "Invalid configuration, must specify both api_key and api_secret or neither"
            )

        if not websocket_auth_token_fetch and api_key and api_secret:

            def default_websocket_auth_token_fetch(wallet_address: str) -> str:
                return RestAuthenticatedClient(
                    api_key=api_key,
                    api_secret=api_secret,
                    multiverse_chain=multiverse_chain,
                    sandbox=sandbox,
                ).get_ws_token(str(uuid1()), wallet_address)

            websocket_auth_token_fetch = default_websocket_auth_token_fetch

        self.base_url = base_url
        self.connect_timeout = 5000 if connect_timeout is None else connect_timeout
        self.should_reconnect_automatically = should_reconnect_automatically
        self.websocket_auth_token_fetch = websocket_auth_token_fetch

    # Connection management

    def is_connected(self) -> bool:
        return self.ws is not None and self.ws.open

    async def connect(self) -> None:
        """
        Establish a WebSocket connection to the API and start listening for messages
        """
        should_wait_for_tasks = not self.state["have_ever_started"]
        self.state["have_ever_started"] = True

        if self.is_connected():
            return

        self.state["do_not_reconnect"] = False

        try:
            self.ws = await ws_connect(self.base_url)
        except Exception as error:
            if self.should_reconnect_automatically and not self.state["do_not_reconnect"]:
                print(
                    f'Failed to connect: "{error}" - '
                    "a reconnect attempt will be scheduled automatically"
                )
                await self.reconnect()
            else:
                raise error

        await self._handle_connect()
        self.state["is_reconnecting"] = False

        await self._run()

        if should_wait_for_tasks:
            # Wait for all tasks to finish
            while self.state["background_tasks"]:
                await next(iter(self.state["background_tasks"]))

    async def _run(self) -> None:
        """
        Run the client, listening for messages, handling them, and handling any connection closures.
        """
        self._raise_if_disconnected()
        assert self.ws

        try:
            while True:
                mesg = await self.ws.recv()
                await self._handle_message(mesg)
        except ConnectionClosed as closed:
            await self._handle_disconnect(closed)
        except Exception as e:
            await self._handle_error(e)

    async def disconnect(self) -> None:
        if not self.ws:
            return
        self.state["do_not_reconnect"] = True
        await self.ws.close()
        self.ws = None

    # Event listeners

    async def _handle_connect(self) -> None:
        self.state["reconnect_attempt"] = 0
        await asyncio.gather(*[listener() for listener in self.state["connect_listeners"]])

    async def _handle_disconnect(self, closed: ConnectionClosed) -> None:
        self.ws = None
        await asyncio.gather(
            *[
                listener(closed.code, closed.reason)
                for listener in self.state["disconnect_listeners"]
            ]
        )

        if self.should_reconnect_automatically and not self.state["do_not_reconnect"]:
            await self.reconnect()

    async def _handle_error(self, e: Exception) -> None:
        await asyncio.gather(*[listener(e) for listener in self.state["error_listeners"]])

    async def _handle_message(self, response: Union[str, bytes]) -> None:
        mesg = transform_websocket_short_response_mesg(json.loads(response))
        await asyncio.gather(*[listener(mesg) for listener in self.state["response_listeners"]])

    def on_connect(self, listener: WebSocketListenerConnect) -> "WebSocketClient":
        self.state["connect_listeners"].add(listener)
        return self

    def on_disconnect(self, listener: WebSocketListenerDisconnect) -> "WebSocketClient":
        self.state["disconnect_listeners"].add(listener)
        return self

    def on_error(self, listener: WebSocketListenerError) -> "WebSocketClient":
        self.state["error_listeners"].add(listener)
        return self

    def on_response(self, listener: WebSocketListenerResponse) -> "WebSocketClient":
        self.state["response_listeners"].add(listener)
        return self

    # Subscription management

    async def list_subscriptions(self) -> None:
        mesg: WebSocketRequestSubscriptions = {"method": "subscriptions"}
        await self._send_message(mesg)

    async def subscribe_authenticated(
        self,
        subscriptions: Sequence[AuthTokenWebSocketRequestAuthenticatedSubscription],
        markets: List[str] = None,
        cid: str = None,
    ) -> None:
        """
        Strictly typed subscribe which only can be used on authenticated subscriptions.

        See https://api-docs-v3.idex.io/#websocket-subscriptions

        Args:
            subscriptions
            markets: Optionally provide top level markets
            cid: Optional custom identifier to identify the matching response
        """
        await self.subscribe(
            subscriptions,
            markets,
            cid,
        )

    async def subscribe_unauthenticated(
        self,
        subscriptions: Sequence[WebSocketRequestUnauthenticatedSubscription],
        markets: List[str] = None,
        cid: str = None,
    ) -> None:
        """
        Strictly typed subscribe which only can be used on non-authenticated subscriptions.

        See https://api-docs-v3.idex.io/#websocket-subscriptions

        Args:
            subscriptions
            markets: Optionally provide top level markets
            cid: Optional custom identifier to identify the matching response
        """
        await self.subscribe(
            subscriptions,
            markets,
            cid,
        )

    async def subscribe(
        self,
        # Must be sequence, not list,
        # see https://github.com/python/mypy/issues/3351#issuecomment-958996686
        subscriptions: Sequence[
            Union[
                WebSocketRequestSubscription,
                WebSocketRequestUnauthenticatedSubscriptionNameOnly,
            ]
        ],
        markets: List[str] = None,
        cid: str = None,
    ) -> None:
        """
        Subscribe to a given set of subscriptions, optionally providing a list of top level markets
        or a cid property.

        See https://api-docs-v3.idex.io/#websocket-subscriptions

        Args:
            subscriptions
            markets: Optionally provide top level markets
            cid: Optional custom identifier to identify the matching response
        """
        # Helper function to reduce code duplication
        def make_subscription_message(
            _subscriptions: Sequence[
                Union[
                    WebSocketRequestSubscription,
                    WebSocketRequestUnauthenticatedSubscriptionNameOnly,
                ]
            ],
        ) -> WebSocketRequestSubscribe:
            mesg: WebSocketRequestSubscribe = {
                "method": "subscribe",
                "subscriptions": _subscriptions,
            }
            if markets:
                mesg["markets"] = markets
            if cid:
                mesg["cid"] = cid
            return mesg

        auth_subscriptions = [
            cast(WebSocketRequestAuthenticatedSubscription, s)
            for s in subscriptions
            if is_websocket_authenticated_subscription(s)
        ]
        if not auth_subscriptions:
            mesg = make_subscription_message(subscriptions)
            await self._send_message(mesg)
            return

        if not self.websocket_auth_token_fetch:
            raise Exception(
                "WebSocket: `websocket_auth_token_fetch` is required "
                "for authenticated subscriptions"
            )

        unique_wallets = list(set(s["wallet"] for s in auth_subscriptions if "wallet" in s))
        if not unique_wallets:
            raise Exception("Missing `wallet` for authenticated subscription")

        # For single wallet, send all subscriptions at once (also unauthenticated)
        if len(unique_wallets) == 1:
            mesg = make_subscription_message(
                list(map(remove_wallet_from_sdk_subscription, subscriptions))
            )
            mesg["token"] = self.websocket_auth_token_fetch(unique_wallets[0])
            await self._send_message(mesg)
            return

        # In specific case when user subscribed with more than 1 wallet...

        # Subscribe public subscriptions all at once
        public_subscriptions = list(filter(is_public_subscription, subscriptions))
        if len(public_subscriptions):
            mesg = make_subscription_message(public_subscriptions)
            await self._send_message(mesg)

        # Send multiple wallets subscriptions grouped by wallet
        for wallet in unique_wallets:
            subs = cast(
                Sequence, list([s for s in auth_subscriptions if s.get("wallet") == wallet])
            )
            subs_no_wallet = list(map(remove_wallet_from_sdk_subscription, subs))
            mesg = make_subscription_message(subs_no_wallet)
            mesg["token"] = self.websocket_auth_token_fetch(wallet)
            await self._send_message(mesg)

        return

    async def unsubscribe(
        self,
        subscriptions: Sequence[
            Union[WebSocketRequestUnsubscribeSubscription, WebSocketRequestUnsubscribeShortNames]
        ],
        markets: List[str] = None,
        cid: str = None,
    ) -> None:
        mesg: WebSocketRequestUnsubscribe = {
            "method": "unsubscribe",
            "subscriptions": subscriptions,
        }
        if markets:
            mesg["markets"] = markets
        if cid:
            mesg["cid"] = cid
        await self._send_message(mesg)
        return

    async def reconnect(self) -> None:
        """
        Reconnect with exponential backoff
        """
        await self.disconnect()
        self.state["do_not_reconnect"] = False
        if not self.state["is_reconnecting"]:
            self.state["is_reconnecting"] = True
            backoff_seconds = 2 ** self.state["reconnect_attempt"]
            self.state["reconnect_attempt"] += 1
            print(f"Reconnecting after {backoff_seconds} seconds...")

            async def wait_and_reconnect() -> None:
                await asyncio.sleep(backoff_seconds)
                await self.connect()

            # Keep track of all running tasks so the top level loop doesn't exit prematurely
            task = asyncio.create_task(wait_and_reconnect())
            task.add_done_callback(self.state["background_tasks"].discard)
            self.state["background_tasks"].add(task)

    def _raise_if_disconnected(self) -> None:
        if not self.is_connected():
            raise Exception("Websocket not yet connected, await connect() method first")

    async def _send_message(self, payload: WebSocketRequest) -> None:
        self._raise_if_disconnected()
        assert self.ws
        await self.ws.send(json.dumps(payload))


# We use this instead of the other type guards to account for unhandled subscription types
def is_public_subscription(
    subscription: Union[
        WebSocketRequestSubscription,
        WebSocketRequestUnauthenticatedSubscriptionNameOnly,
    ]
) -> bool:
    return not is_websocket_authenticated_subscription(subscription)
