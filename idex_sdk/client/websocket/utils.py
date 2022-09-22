from typing import Union, cast

from idex_sdk.idex_types.websocket.request import (
    WebSocketRequestSubscription,
    WebSocketRequestUnauthenticatedSubscriptionNameOnly,
)


# Wallet is used only to generate user's wallet auth token
# After we got token, we don't want to send wallet to the server
def remove_wallet_from_sdk_subscription(
    subscription: Union[
        WebSocketRequestUnauthenticatedSubscriptionNameOnly, WebSocketRequestSubscription
    ],
) -> Union[WebSocketRequestUnauthenticatedSubscriptionNameOnly, WebSocketRequestSubscription]:
    if type(subscription) == str:
        return subscription
    subscription_without_wallet = cast(WebSocketRequestSubscription, {**subscription})
    if "wallet" in subscription_without_wallet:
        del subscription_without_wallet["wallet"]
    return subscription_without_wallet
