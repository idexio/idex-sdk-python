import unittest

from idex_sdk import signatures as sig
from idex_sdk.idex_types import enums
from idex_sdk.idex_types.rest.request import (
    RestRequestAddLiquidity,
    RestRequestAssociateWallet,
    RestRequestCancelOrder,
    RestRequestCancelOrders,
    RestRequestLimitOrderByBaseQuantity,
    RestRequestLimitOrderByQuoteQuantity,
    RestRequestRemoveLiquidity,
    RestRequestWithdrawalByAddress,
    RestRequestWithdrawalBySymbol,
)


class TestSignatures(unittest.TestCase):
    uuid = "e10cdc00-e1fb-11ec-9ae3-e11f6164b292"
    wallet_addr = "0x13ccbb6a85aec077da32c7078e83a70bbb70a6dd"
    weth_addr = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    usdc_addr = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"

    # The private key is for a very public Hardhat account, so ok to commit
    hh_acc0_pk = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
    hh_acc0_addr = "0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266"

    def test_solidity_hash_of_params(self) -> None:
        hash_ = sig.solidity_hash_of_params(
            [
                ("string", "abc"),
                ("address", self.wallet_addr),
                ("uint128", sig.uuid_to_int(self.uuid)),
                ("uint8", 42),
                ("uint64", 9),
                ("bool", True),
                ("uint256", "15"),
                ("uint256", 15),
            ]
        )
        self.assertEqual(
            hash_, "0xde2e6d9520c6946d64a2c72dae9cd9b9f55db825f711119f33d3377499becfa6"
        )

    def test_create_order_signature_hash(self) -> None:
        req1: RestRequestLimitOrderByBaseQuantity = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "market": "ETH-USDC",
            "type": "limit",
            "side": "buy",
            "price": "100",
            "quantity": "100",
        }
        hash_ = sig.create_order_signature_hash(req1, enums.MultiverseChain.MATIC, False)
        self.assertEqual(
            hash_, "0xadeb081efc10b788d811bda7ebfb964afa9d4438cc0d7d58ab0268c6986fa976"
        )

        req2: RestRequestLimitOrderByQuoteQuantity = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "market": "ETH-USDC",
            "type": "limit",
            "side": "buy",
            "price": "100",
            "quoteOrderQuantity": "100",
        }
        hash_ = sig.create_order_signature_hash(req2, enums.MultiverseChain.MATIC, False)
        self.assertEqual(
            hash_, "0x6dc7bb86c7663ab6ab34cf752dd7f9d05ed54e0be7c39b8d5dce10e40ae38dd0"
        )

    def test_create_cancel_order_signature_hash(self) -> None:
        req1: RestRequestCancelOrder = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "orderId": "123",
        }
        hash_ = sig.create_cancel_order_signature_hash(req1)
        self.assertEqual(
            hash_, "0x5ab589811bcb63397c7fb5b678428d2de0ed7a20a0abe806820587678f3bb951"
        )

        req2: RestRequestCancelOrders = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "market": "ETH-USDC",
        }
        hash_ = sig.create_cancel_order_signature_hash(req2)
        self.assertEqual(
            hash_, "0xa2121f207842720121e071ad9c1df301b594c6a687cc06074524131eda6a33f9"
        )

    def test_create_withdrawal_signature_hash(self) -> None:
        req1: RestRequestWithdrawalBySymbol = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "quantity": "100",
            "asset": "USDC",
        }
        hash_ = sig.create_withdrawal_signature_hash(req1)
        self.assertEqual(
            hash_, "0xb9ac734609697bcdbda9f45fb052c8ccaeceec2f45329d628caceb54a6f50282"
        )

        req2: RestRequestWithdrawalByAddress = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "quantity": "100",
            "assetContractAddress": self.usdc_addr,
        }
        hash_ = sig.create_withdrawal_signature_hash(req2)
        self.assertEqual(
            hash_, "0xa4d8fa53fcab69ec85286538bd46f9a6c817848e89a02fcd21c37f8e66e391f4"
        )

    def test_create_add_liquidity_signature_hash(self) -> None:
        req: RestRequestAddLiquidity = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "tokenA": self.weth_addr,
            "tokenB": self.usdc_addr,
            "amountADesired": "200",
            "amountBDesired": "200",
            "amountAMin": "100",
            "amountBMin": "100",
            "to": self.wallet_addr,
        }
        hash_ = sig.create_add_liquidity_signature_hash(req, enums.MultiverseChain.MATIC, False)
        self.assertEqual(
            hash_, "0x21686951d00e3100586a6cac9772db870934f1eae2582e61b976847488082f44"
        )

    def test_create_remove_liquidity_signature_hash(self) -> None:
        req: RestRequestRemoveLiquidity = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
            "tokenA": self.weth_addr,
            "tokenB": self.usdc_addr,
            "liquidity": "100",
            "amountAMin": "100",
            "amountBMin": "100",
            "to": self.wallet_addr,
        }
        hash_ = sig.create_remove_liquidity_signature_hash(req, enums.MultiverseChain.MATIC, False)
        self.assertEqual(
            hash_, "0x52fa5ce02d8336d2ab6fac2461b6c9bf49d24fc3a0c3e9608f776105de7a4c2b"
        )

    def test_create_associate_wallet_signature_hash(self) -> None:
        req: RestRequestAssociateWallet = {
            "nonce": self.uuid,
            "wallet": self.wallet_addr,
        }
        hash_ = sig.create_associate_wallet_signature_hash(req)
        self.assertEqual(
            hash_, "0x4ed7c2514c07348e6bb566607929dfb7e5e451acd852f193ba0516e674873741"
        )

    def test_create_private_key_message_signer(self) -> None:
        signer = sig.create_private_key_message_signer(self.hh_acc0_pk)
        signature = signer("0x4ed7c2514c07348e6bb566607929dfb7e5e451acd852f193ba0516e674873741")
        self.assertEqual(
            signature,
            "0x472d93e58fb0f8840f6441bee86d9079310f10c0737d01c15715e53761751d764eaa8d9ce97d9cfdef0f79007eaf5e900743d86f38e1c0f851b90e87a0f2736f1b",
        )
