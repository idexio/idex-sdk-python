from idex_sdk.idex_types.rest.request import (
    RestRequestCancelOrderOrOrders,
    RestRequestOrder,
    RestRequestWithdrawal,
)


def is_rest_request_order_by_base_quantity(
    req: RestRequestOrder,
) -> bool:
    quantity = req.get("quantity")
    quote_order_quantity = req.get("quoteOrderQuantity")
    return isinstance(quantity, str) and not isinstance(quote_order_quantity, str)


def is_rest_request_order_by_quote_quantity(
    req: RestRequestOrder,
) -> bool:
    quantity = req.get("quantity")
    quote_order_quantity = req.get("quoteOrderQuantity")
    return not isinstance(quantity, str) and isinstance(quote_order_quantity, str)


def is_rest_request_withdrawal_by_symbol(
    req: RestRequestWithdrawal,
) -> bool:
    asset = req.get("asset")
    asset_contract_address = req.get("assetContractAddress")
    return isinstance(asset, str) and not isinstance(asset_contract_address, str)


def is_rest_request_withdrawal_by_address(
    req: RestRequestWithdrawal,
) -> bool:
    asset = req.get("asset")
    asset_contract_address = req.get("assetContractAddress")
    return not isinstance(asset, str) and isinstance(asset_contract_address, str)


def is_rest_request_cancel_order(req: RestRequestCancelOrderOrOrders) -> bool:
    order_id = req.get("orderId")
    market = req.get("market")
    return isinstance(order_id, str) and market is None


def is_rest_request_cancel_orders(req: RestRequestCancelOrderOrOrders) -> bool:
    order_id = req.get("orderId")
    return order_id is None
