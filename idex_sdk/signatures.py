from typing import Callable, List, Literal, Tuple, Union, cast

from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3

from idex_sdk.idex_types.enums import (
    ORDER_SELF_TRADE_PREVENTION_IDS,
    ORDER_SIDE_IDS,
    ORDER_TIME_IN_FORCE_IDS,
    ORDER_TYPE_IDS,
    LiquidityChangeOrigination,
    LiquidityChangeType,
    MultiverseChain,
    OrderSignatureHashVersion,
)
from idex_sdk.idex_types.rest.guards import (
    is_rest_request_cancel_order,
    is_rest_request_cancel_orders,
    is_rest_request_order_by_base_quantity,
    is_rest_request_order_by_quote_quantity,
    is_rest_request_withdrawal_by_address,
    is_rest_request_withdrawal_by_symbol,
)
from idex_sdk.idex_types.rest.request import (
    RestRequestAddLiquidity,
    RestRequestAssociateWallet,
    RestRequestCancelOrder,
    RestRequestCancelOrderOrOrders,
    RestRequestCancelOrders,
    RestRequestOrder,
    RestRequestOrderByBaseQuantity,
    RestRequestOrderByQuoteQuantity,
    RestRequestRemoveLiquidity,
    RestRequestWithdrawal,
    RestRequestWithdrawalByAddress,
    RestRequestWithdrawalBySymbol,
)

# A function that accepts a message and returns its ECDSA signature
MessageSigner = Callable[[str], str]


def create_private_key_message_signer(wallet_private_key: str) -> MessageSigner:
    """
    Returns a function which signs a message with the originally provided private key.

    Args:
        wallet_private_key: Private key to use when signing messages

    Returns:
        The message signing function
    """
    account = Account.from_key(wallet_private_key)
    return lambda msg: account.sign_message(encode_defunct(hexstr=msg)).signature.hex()


def signature_hash_version(
    multiverse_chain: MultiverseChain, sandbox: bool
) -> OrderSignatureHashVersion:
    if multiverse_chain == MultiverseChain.MATIC:
        if sandbox:
            return OrderSignatureHashVersion.MATIC_SANDBOX
        return OrderSignatureHashVersion.MATIC
    raise Exception(f"Invalid multiverse chain: {multiverse_chain}")


def create_order_signature_hash(
    req: RestRequestOrder,
    multiverse_chain: MultiverseChain,
    sandbox: bool,
) -> str:
    # Determine whether req is a RestRequestOrderByBaseQuantity or a RestRequestOrderByQuoteQuantity
    if is_rest_request_order_by_base_quantity(req):
        req = cast(RestRequestOrderByBaseQuantity, req)
        quantity = req["quantity"]
        is_quantity_for_quote = False
    elif is_rest_request_order_by_quote_quantity:
        req = cast(RestRequestOrderByQuoteQuantity, req)
        quantity = req["quoteOrderQuantity"]
        is_quantity_for_quote = True
    else:
        raise Exception(
            "Request is neither a RestRequestOrderByBaseQuantity "
            "nor a RestRequestOrderByQuoteQuantity"
        )

    return solidity_hash_of_params(
        [
            ("uint8", signature_hash_version(multiverse_chain, sandbox).value),
            ("uint128", uuid_to_int(req["nonce"])),
            ("address", req["wallet"]),
            ("string", req["market"]),
            ("uint8", ORDER_TYPE_IDS[req["type"]]),
            ("uint8", ORDER_SIDE_IDS[req["side"]]),
            ("string", quantity),
            ("bool", is_quantity_for_quote),
            ("string", cast(str, req.get("price", ""))),
            ("string", cast(str, req.get("stopPrice", ""))),
            ("string", req.get("clientOrderId", "")),
            ("uint8", ORDER_TIME_IN_FORCE_IDS[req["timeInForce"]] if "timeInForce" in req else 0),
            (
                "uint8",
                (
                    ORDER_SELF_TRADE_PREVENTION_IDS[req["selfTradePrevention"]]
                    if "selfTradePrevention" in req
                    else 0
                ),
            ),
            ("uint64", req.get("cancelAfter", 0)),
        ]
    )


def create_cancel_order_signature_hash(req: RestRequestCancelOrderOrOrders) -> str:
    # Determine whether req is a RestRequestCancelOrder or a RestRequestCancelOrders
    if is_rest_request_cancel_order(req):
        req = cast(RestRequestCancelOrder, req)
        order_id = req["orderId"]
        market = ""
    elif is_rest_request_cancel_orders(req):
        req = cast(RestRequestCancelOrders, req)
        order_id = ""
        market = req.get("market", "")
    else:
        raise Exception("Request is neither a RestRequestCancelOrder nor a RestRequestCancelOrders")

    return solidity_hash_of_params(
        [
            ("uint128", uuid_to_int(req["nonce"])),
            ("address", req["wallet"]),
            ("string", order_id),
            ("string", market),
        ]
    )


def create_withdrawal_signature_hash(req: RestRequestWithdrawal) -> str:
    # Determine whether req is a RestRequestWithdrawalBySymbol or a RestRequestWithdrawalByAddress
    withdrawal_solidity_param_tuple: SolidityParamTuple
    if is_rest_request_withdrawal_by_symbol(req):
        req = cast(RestRequestWithdrawalBySymbol, req)
        withdrawal_solidity_param_tuple = ("string", req["asset"])
    elif is_rest_request_withdrawal_by_address(req):
        req = cast(RestRequestWithdrawalByAddress, req)
        withdrawal_solidity_param_tuple = ("address", req["assetContractAddress"])
    else:
        raise Exception(
            "Request is neither a RestRequestWithdrawalBySymbol "
            "nor a RestRequestWithdrawalByAddress"
        )

    return solidity_hash_of_params(
        [
            ("uint128", uuid_to_int(req["nonce"])),
            ("address", req["wallet"]),
            withdrawal_solidity_param_tuple,
            ("string", req["quantity"]),
            ("bool", True),  # Auto-dispatch
        ]
    )


def create_add_liquidity_signature_hash(
    req: RestRequestAddLiquidity,
    multiverse_chain: MultiverseChain,
    sandbox: bool,
) -> str:
    return solidity_hash_of_params(
        [
            ("uint8", signature_hash_version(multiverse_chain, sandbox).value),
            ("uint8", LiquidityChangeType.ADDITION.value),
            ("uint8", LiquidityChangeOrigination.OFFCHAIN.value),
            ("uint128", uuid_to_int(req["nonce"])),
            ("address", req["wallet"]),
            ("address", req["tokenA"]),
            ("address", req["tokenB"]),
            ("uint256", req["amountADesired"]),
            ("uint256", req["amountBDesired"]),
            ("uint256", req["amountAMin"]),
            ("uint256", req["amountBMin"]),
            ("address", req["to"]),
            ("uint256", "0"),  # Off-chain deadline
        ]
    )


def create_remove_liquidity_signature_hash(
    req: RestRequestRemoveLiquidity,
    multiverse_chain: MultiverseChain,
    sandbox: bool,
) -> str:
    return solidity_hash_of_params(
        [
            ("uint8", signature_hash_version(multiverse_chain, sandbox).value),
            ("uint8", LiquidityChangeType.REMOVAL.value),
            ("uint8", LiquidityChangeOrigination.OFFCHAIN.value),
            ("uint128", uuid_to_int(req["nonce"])),
            ("address", req["wallet"]),
            ("address", req["tokenA"]),
            ("address", req["tokenB"]),
            ("uint256", req["liquidity"]),
            ("uint256", req["amountAMin"]),
            ("uint256", req["amountBMin"]),
            ("address", req["to"]),
            ("uint256", "0"),  # Off-chain deadline
        ]
    )


def create_associate_wallet_signature_hash(
    associate: RestRequestAssociateWallet,
) -> str:
    return solidity_hash_of_params(
        [
            ("uint128", uuid_to_int(associate["nonce"])),
            ("address", associate["wallet"]),
        ]
    )


def uuid_to_int(uuid: str) -> int:
    return int(uuid.replace("-", ""), 16)


SolidityStringParamTuple = Tuple[Literal["string"], str]
SolidityAddressParamTuple = Tuple[Literal["address"], str]
SolidityUint128ParamTuple = Tuple[Literal["uint128"], int]
SolidityUint8ParamTuple = Tuple[Literal["uint8"], int]
SolidityUint64ParamTuple = Tuple[Literal["uint64"], int]
SolidityBoolParamTuple = Tuple[Literal["bool"], bool]

# Uint256s can be passed as ints or strs, if str will be auto converted to int before hashing
SolidityUint256StrParamTuple = Tuple[Literal["uint256"], str]
SolidityUint256IntParamTuple = Tuple[Literal["uint256"], int]

SolidityParamTuple = Union[
    SolidityStringParamTuple,
    SolidityAddressParamTuple,
    SolidityUint128ParamTuple,
    SolidityUint8ParamTuple,
    SolidityUint64ParamTuple,
    SolidityUint256StrParamTuple,
    SolidityUint256IntParamTuple,
    SolidityBoolParamTuple,
]


def solidity_hash_of_params(params: List[SolidityParamTuple]) -> str:
    for i, (typ, val) in enumerate(params):
        # Make sure all addresses are checksummed
        if typ == "address":
            val = cast(str, val)
            params[i] = ("address", Web3.toChecksumAddress(val))
        # Convert SolidityUint256StrParamTuple to SolidityUint256IntParamTuple
        elif typ == "uint256" and isinstance(val, str):
            params[i] = ("uint256", int(val))

    types, values = zip(*params)
    return Web3.solidityKeccak(types, values).hex()
