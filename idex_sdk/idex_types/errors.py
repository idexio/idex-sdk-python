from typing import Literal

from requests import Response

# The possible error short codes when interacting with the IDEX API's.
ErrorShortCodes = Literal[
    "TOKEN_NOT_FOUND",
    "ORDER_NOT_FOUND",
    "MARKET_NOT_FOUND",
    "DEPOSIT_NOT_FOUND",
    "WITHDRAWAL_NOT_FOUND",
    "FILL_NOT_FOUND",
    "USER_NOT_FOUND",
    "ENDPOINT_NOT_FOUND",
    "EXCEEDED_RATE_LIMIT",
    "INSUFFICIENT_FUNDS",
    "USER_MIGRATION_REQUIRED",
    "WALLET_NOT_ASSOCIATED",
    "EMAIL_VERIFICATION_REQUIRED",
    "INVALID_WALLET_SIGNATURE",
    "INVALID_API_KEY",
    "REQUIRED_API_KEY",
    "INVALID_HMAC_SIGNATURE",
    "REQUIRED_HMAC_SIGNATURE",
    "REQUIRED_API_KEY_READ_SCOPE",
    "REQUIRED_API_KEY_TRADE_SCOPE",
    "REQUIRED_API_KEY_WITHDRAW_SCOPE",
    "TRADING_RESTRICTED_FOR_LOCATION",
    "EXCEEDED_WITHDRAWAL_LIMIT",
    "CANCELS_DISABLED",
    "TRADING_DISABLED",
    "WITHDRAWALS_DISABLED",
    "INTERNAL_SERVER_ERROR",
    "BAD_REQUEST",
    "SERVICE_UNAVAILABLE",
    "INVALID_API_VERSION",
    "REQUIRED_PARAMETER",
    "INVALID_PARAMETER",
    "INVALID_WITHDRAWAL_QUANTITY",
    "INVALID_ORDER_QUANTITY",
    "INVALID_ORDER_PRICE_CROSSES_SPREAD",
]


class IdexApiError(Exception):
    status_code: int


class BadRequestError(IdexApiError):
    status_code = 400


class TooManyRequestsError(IdexApiError):
    status_code = 429


class InternalServerError(IdexApiError):
    status_code = 500


API_ERRORS_BY_STATUS_CODE = {
    400: BadRequestError,
    429: TooManyRequestsError,
    500: InternalServerError,
}


def check_response_errors(response: Response) -> None:
    if response.status_code != 200:
        ErrorClass = API_ERRORS_BY_STATUS_CODE.get(response.status_code)
        if ErrorClass:
            raise ErrorClass(response.text)
        raise Exception(f"Error {response.status_code}: {response.text}")
