from typing import Dict, Literal

from idex_sdk.idex_types.enums import MultiverseChain

REST_API_KEY_HEADER = "IDEX-API-Key"
REST_HMAC_SIGNATURE_HEADER = "IDEX-HMAC-Signature"

ORDER_BOOK_MAX_L2_LEVELS = 500

ORDER_BOOK_FIRST_LEVEL_MULTIPLIER_IN_PIPS = 110000000  # 1.1x

ORDER_BOOK_HYBRID_SLIPPAGE = 100  # 0.1%


# The URI that will be used based on the configuration given.  This includes
# sandbox vs production as well as the multi-verse chain that should be used
# (eth default for all clients).
#
# See:
# https://api-docs-v3.idex.io/#websocket-api-interaction
# https://api-docs-v3.idex.io/#rest-api-interaction
# https://api-docs-v3.idex.io/#sandbox
#
URLS: Dict[
    Literal["sandbox", "production"], Dict[MultiverseChain, Dict[Literal["rest", "websocket"], str]]
] = {
    "sandbox": {
        MultiverseChain.MATIC: {
            "rest": "https://api-sandbox-matic.idex.io/v1",
            "websocket": "wss://websocket-sandbox-matic.idex.io/v1",
        },
    },
    "production": {
        MultiverseChain.MATIC: {
            "rest": "https://api-matic.idex.io/v1",
            "websocket": "wss://websocket-matic.idex.io/v1",
        },
    },
}
