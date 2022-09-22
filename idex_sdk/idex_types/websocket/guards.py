from typing import Any

from idex_sdk.idex_types.websocket.constants import (
    WEBSOCKET_AUTHENTICATED_SUBSCRIPTIONS,
)


def is_websocket_authenticated_subscription(subscription: Any) -> bool:
    return (
        subscription
        and isinstance(subscription, dict)
        and "name" in subscription
        and subscription["name"] in WEBSOCKET_AUTHENTICATED_SUBSCRIPTIONS
    )
