import hmac
from typing import Dict, Literal, Optional

from idex_sdk_python.constants import REST_HMAC_SIGNATURE_HEADER, URLS
from idex_sdk_python.idex_types.enums import MultiverseChain


def derive_base_url(
    api_type: Literal["rest", "websocket"],
    multiverse_chain: MultiverseChain = MultiverseChain.MATIC,
    sandbox: bool = False,
    override_base_url: Optional[str] = None,
) -> str:
    if override_base_url:
        base_url = override_base_url
        if base_url[-1] == "/":
            base_url = base_url[:-1]
        return base_url
    try:
        return URLS["sandbox" if sandbox else "production"][multiverse_chain][api_type]
    except KeyError:
        raise Exception(
            f"Invalid configuration, base_url could not be derived "
            f"(sandbox? {sandbox}, chain: {multiverse_chain.value})"
        )


def create_hmac_rest_request_signature_header(secret: str, payload: str) -> Dict[str, str]:
    sig = hmac.new(key=secret.encode(), msg=payload.encode(), digestmod="sha256").hexdigest()
    return {REST_HMAC_SIGNATURE_HEADER: sig}
