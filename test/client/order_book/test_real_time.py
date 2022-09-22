import json
import os
import unittest
from typing import Any
from unittest.mock import MagicMock

from idex_sdk.client.order_book.real_time import OrderBookRealTimeClient

file_dir = os.path.dirname(os.path.abspath(__file__))


class TestRestAuthenticatedClient(unittest.IsolatedAsyncioTestCase):
    maxDiff = None

    @staticmethod
    async def get_client(order_book: Any) -> OrderBookRealTimeClient:
        async def async_nothing():
            pass

        client = OrderBookRealTimeClient()
        client.rest_public_client = MagicMock()
        client.rest_public_client.get_exchange_info.return_value = {
            "timeZone": "UTC",
            "serverTime": 1663357542131,
            "maticDepositContractAddress": "0x3253a7e75539edaeb1db608ce6ef9aa1ac9126b6",
            "maticCustodyContractAddress": "0x3bcc4eca0a40358558ca8d1bcd2d1dbde63eb468",
            "maticUsdPrice": "0.80",
            "gasPrice": 142,
            "volume24hUsd": "8660945.39",
            "totalVolumeUsd": "2548127401.77",
            "totalTrades": 1952730,
            "totalValueLockedUsd": "7572470.31",
            "idexStakingValueLockedUsd": "17502177.51",
            "idexTokenAddress": "0x9Cb74C8032b007466865f060ad2c46145d45553D",
            "idexUsdPrice": "0.06",
            "idexMarketCapUsd": "43431211.00",
            "makerFeeRate": "0.0000",
            "takerFeeRate": "0.0025",
            "takerIdexFeeRate": "0.0005",
            "takerLiquidityProviderFeeRate": "0.0020",
            "makerTradeMinimum": "10.00000000",
            "takerTradeMinimum": "1.00000000",
            "withdrawMinimum": "0.50000000",
            "liquidityAdditionMinimum": "0.50000000",
            "liquidityRemovalMinimum": "0.40000000",
            "blockConfirmationDelay": 64,
        }

        client.rest_public_client.get_assets.return_value = [
            {
                "name": "USD Coin",
                "symbol": "USDC",
                "contractAddress": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                "assetDecimals": 6,
                "exchangeDecimals": 8,
                "maticPrice": "1.24223602",
            }
        ]
        client.rest_public_client.get_markets.return_value = [
            {
                "market": "IDEX-USDC",
                "type": "hybrid",
                "status": "activeHybrid",
                "baseAsset": "IDEX",
                "baseAssetPrecision": 8,
                "quoteAsset": "USDC",
                "quoteAssetPrecision": 8,
                "makerFeeRate": "0.0000",
                "takerFeeRate": "0.2500",
                "takerIdexFeeRate": "0.0500",
                "takerLiquidityProviderFeeRate": "0.2000",
                "tickSize": "0.00001000",
            }
        ]
        client.rest_public_client.get_order_book_level2.return_value = order_book
        client.websocket_client = MagicMock()
        client.websocket_client.connect = async_nothing
        await client.start(["IDEX-USDC"])
        await client.load_fees_and_minimums()
        await client.load_token_prices()
        await client.load_tick_sizes()
        return client

    async def test_get_order_book_l2_1(self):
        with open(f"{file_dir}/sequence_1130790.json") as json_file:
            rest_order_book = json.load(json_file)
        client = await self.get_client(rest_order_book)
        order_book = client.get_order_book_l2("IDEX-USDC", 10)
        self.assertEqual(
            order_book,
            {
                "asks": [
                    ["0.06598000", "332.64912641", 0],
                    ["0.06604000", "1994.30622784", 0],
                    ["0.06611000", "2323.25486396", 0],
                    ["0.06618000", "2319.56416981", 0],
                    ["0.06625000", "2315.88323482", 0],
                ],
                "bids": [
                    ["0.06596000", "332.72480908", 0],
                    ["0.06590000", "1997.93900807", 0],
                    ["0.06583000", "2334.38028034", 0],
                    ["0.06576000", "2338.10663115", 0],
                    ["0.06569000", "2341.84290642", 0],
                ],
                "pool": {
                    "baseReserveQuantity": "4382887.83017307",
                    "quoteReserveQuantity": "289139.11015652",
                },
                "sequence": 1130790,
            },
        )
        del client

    async def test_get_order_book_l2_2(self):
        with open(f"{file_dir}/sequence_1139290.json") as json_file:
            rest_order_book = json.load(json_file)
        client = await self.get_client(rest_order_book)
        order_book = client.get_order_book_l2("IDEX-USDC", 10)
        self.assertEqual(
            order_book,
            {
                "asks": [
                    ["0.06435000", "306.19302271", 0],
                    ["0.06440000", "1748.98185427", 0],
                    ["0.06446000", "2096.08879782", 0],
                    ["0.06452000", "2093.16132637", 0],
                    ["0.06458000", "2090.24066105", 0],
                ],
                "bids": [
                    ["0.06434000", "43.84822131", 0],
                    ["0.06428000", "2101.96271577", 0],
                    ["0.06422000", "2104.90778815", 0],
                    ["0.06416000", "2107.85974423", 0],
                    ["0.06410000", "2110.81860655", 0],
                ],
                "pool": {
                    "baseReserveQuantity": "4498055.11517087",
                    "quoteReserveQuantity": "289410.50006305",
                },
                "sequence": 1139290,
            },
        )
        del client


if __name__ == "__main__":
    unittest.main()
