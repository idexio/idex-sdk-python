import unittest

from idex_sdk_python.client.utils import create_hmac_rest_request_signature_header
from idex_sdk_python.constants import REST_HMAC_SIGNATURE_HEADER


class TestClientUtils(unittest.TestCase):
    hmac_secret = "7ec325085c834e60"

    def test_create_hmac_rest_request_signature_header(self) -> None:
        sig_header = create_hmac_rest_request_signature_header(
            secret=self.hmac_secret, payload="test_payload"
        )
        self.assertEqual(
            sig_header[REST_HMAC_SIGNATURE_HEADER],
            "fe6d8a0e3c8f88d1f9dc8d0f02a909cd4875bd36c22aba62b1a5407fc0bf363f",
        )
