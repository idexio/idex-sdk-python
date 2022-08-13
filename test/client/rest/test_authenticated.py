import unittest

from idex_sdk_python.client.rest.authenticated import RestAuthenticatedClient
from idex_sdk_python.constants import REST_HMAC_SIGNATURE_HEADER


class TestRestAuthenticatedClient(unittest.TestCase):
    api_key = "api_key"
    api_secret = "864bbe8797574d9f"

    def get_client(self) -> RestAuthenticatedClient:
        return RestAuthenticatedClient(api_key=self.api_key, api_secret=self.api_secret)

    def test_create_request_signature_header_get(self) -> None:
        client = self.get_client()
        header = client._create_request_signature_header("GET", params={"param1": 1, "param2": "2"})
        self.assertEqual(
            header[REST_HMAC_SIGNATURE_HEADER],
            "7e5fa1716e604a8141daa5352334c7b2eb52dde33039d8b7c5ffd1da955b14f5",
        )

    def test_create_request_signature_header_post(self) -> None:
        client = self.get_client()
        header = client._create_request_signature_header(
            "POST", json={"param1": 1, "param2": ["1", "2", "3"]}
        )
        self.assertEqual(
            header[REST_HMAC_SIGNATURE_HEADER],
            "38cdb28adc6f8448670a3814d129fd08f3d07d852e7e74e77ec7f1185a11f13f",
        )
