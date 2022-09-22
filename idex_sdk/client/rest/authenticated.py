import json
from typing import Any, Dict, List, Literal, Optional, Union, cast
from urllib.parse import urlencode

import requests

from idex_sdk import signatures as sig
from idex_sdk.client.utils import (
    create_hmac_rest_request_signature_header,
    derive_base_url,
)
from idex_sdk.constants import REST_API_KEY_HEADER
from idex_sdk.idex_types.enums import MultiverseChain
from idex_sdk.idex_types.errors import check_response_errors
from idex_sdk.idex_types.rest import request, response

RequestMethodTypes = Literal["GET", "POST", "PUT", "DELETE", "PATCH"]


class RestAuthenticatedClient:
    base_url: str
    api_secret: Optional[str]
    signer: Optional[sig.MessageSigner] = None
    multiverse_chain: MultiverseChain
    sandbox: bool
    session: requests.Session

    def __init__(
        self,
        api_key: Optional[str],
        api_secret: Optional[str],
        wallet_private_key: Optional[str] = None,
        multiverse_chain: MultiverseChain = MultiverseChain.MATIC,
        sandbox: bool = False,
        base_url: Optional[str] = None,
    ) -> None:
        self.base_url = derive_base_url(
            api_type="rest",
            multiverse_chain=multiverse_chain,
            sandbox=sandbox,
            override_base_url=base_url,
        )
        self.api_secret = api_secret
        self.multiverse_chain = multiverse_chain
        self.sandbox = sandbox
        if wallet_private_key:
            self.signer = sig.create_private_key_message_signer(wallet_private_key)
        self.session = requests.Session()
        if api_key:
            self.session.headers[REST_API_KEY_HEADER] = api_key

    def _create_request_signature_header(
        self, method: RequestMethodTypes, **kwargs: Any
    ) -> Dict[str, str]:
        if method == "GET":
            payload = urlencode(kwargs["params"])
        else:
            payload = json.dumps(kwargs["json"], separators=(",", ":"))
        return create_hmac_rest_request_signature_header(
            secret=cast(str, self.api_secret), payload=payload
        )

    def _request(self, method: RequestMethodTypes, endpoint: str, **kwargs: Any) -> Any:
        headers = dict(self.session.headers)
        headers.update(self._create_request_signature_header(method, **kwargs))
        res = self.session.request(method, self.base_url + endpoint, headers=headers, **kwargs)
        check_response_errors(res)
        return res.json()

    def _get(self, endpoint: str, params: Any = None) -> Any:
        return self._request("GET", endpoint, params=params)

    def _post(self, endpoint: str, json: Any = None) -> Any:
        return self._request("POST", endpoint, json=json)

    def _delete(self, endpoint: str, json: Any = None) -> Any:
        return self._request("DELETE", endpoint, json=json)

    def _check_signer(self, signer: Optional[sig.MessageSigner]) -> sig.MessageSigner:
        if not signer:
            signer = self.signer
        if not signer:
            raise Exception(
                "A 'signer' function is required but was not provided during "
                "RestAuthenticatedClient constructor or when calling the method"
            )
        return signer

    def add_liquidity(
        self,
        req: request.RestRequestAddLiquidity,
        signer: Optional[sig.MessageSigner] = None,
        dependent_transactions: Optional[List[str]] = None,
    ) -> response.RestResponseLiquidityAddition:
        """
        Add liquidity to a hybrid liquidity pool from assets held by a wallet on the exchange
        """
        signer = self._check_signer(signer)
        data = {
            "parameters": req,
            "signature": signer(
                sig.create_add_liquidity_signature_hash(
                    req,
                    multiverse_chain=self.multiverse_chain,
                    sandbox=self.sandbox,
                )
            ),
        }
        if dependent_transactions:
            data["dependentTransactions"] = dependent_transactions
        return self._post("/addLiquidity", data)

    def remove_liquidity(
        self,
        req: request.RestRequestRemoveLiquidity,
        signer: Optional[sig.MessageSigner] = None,
        dependent_transactions: Optional[List[str]] = None,
    ) -> response.RestResponseLiquidityRemoval:
        """
        Remove liquidity from a hybrid liquidity pool represented by LP tokens held by a wallet
        on the exchange
        """
        signer = self._check_signer(signer)
        data = {
            "parameters": req,
            "signature": signer(
                sig.create_remove_liquidity_signature_hash(
                    req,
                    multiverse_chain=self.multiverse_chain,
                    sandbox=self.sandbox,
                )
            ),
        }
        if dependent_transactions:
            data["dependentTransactions"] = dependent_transactions
        return self._post("/removeLiquidity", data)

    def get_liquidity_addition(
        self,
        req: request.RestRequestFindLiquidityAddition,
    ) -> Union[
        response.RestResponseLiquidityAddition, List[response.RestResponseLiquidityAddition]
    ]:
        """
        Returns information about a single liquidity addition from a wallet
        """
        return self._get("/liquidityAdditions", req)

    def get_liquidity_additions(
        self,
        req: request.RestRequestFindLiquidityChanges,
    ) -> List[response.RestResponseLiquidityAddition]:
        """
        Returns information about multiple liquidity additions from a wallet
        """
        return self._get("/liquidityAdditions", req)

    def get_liquidity_removal(
        self,
        req: request.RestRequestFindLiquidityRemoval,
    ) -> response.RestResponseLiquidityRemoval:
        """
        Returns information about a single liquidity removal from a wallet
        """
        return self._get("/liquidityRemovals", req)

    def get_liquidity_removals(
        self,
        req: request.RestRequestFindLiquidityChanges,
    ) -> List[response.RestResponseLiquidityRemoval]:
        """
        Returns information about multiple liquidity removals from a wallet
        """
        return self._get("/liquidityRemovals", req)

    # User Data Endpoints

    def get_user(self, nonce: str) -> response.RestResponseUser:
        """
        Get account details for the API key's user
        See https://api-docs-v3.idex.io/#get-user-account

        Args:
            nonce: UUIDv1

        Returns:
            Information about the user
        """
        return self._get("/user", {"nonce": nonce})

    def get_wallets(self, nonce: str) -> List[response.RestResponseWallet]:
        """
        Get account details for the API key's user
        See https://api-docs-v3.idex.io/#get-wallets

        Args:
            nonce: UUIDv1

        Returns:
            The user's wallets
        """
        return self._get("/wallets", {"nonce": nonce})

    def get_balances(
        self, req: request.RestRequestFindBalances
    ) -> List[response.RestResponseBalance]:
        """
        Get asset quantity data (positions) held by a wallet on the exchange
        """
        return self._get("/balances", req)

    # Wallet Association Endpoint

    def associate_wallet(
        self, req: request.RestRequestAssociateWallet, signer: Optional[sig.MessageSigner] = None
    ) -> response.RestResponseAssociateWallet:
        """
        Associate a wallet with the authenticated account
        See https://api-docs-v3.idex.io/#associate-wallet
        """
        signer = self._check_signer(signer)
        return self._post(
            "/wallets",
            {
                "parameters": req,
                "signature": signer(sig.create_associate_wallet_signature_hash(req)),
            },
        )

    # Orders & Trade Endpoints

    def create_order(
        self, req: request.RestRequestOrder, signer: Optional[sig.MessageSigner] = None
    ) -> response.RestResponseOrder:
        """
        Create and submit an order to the matching engine
        See https://api-docs-v3.idex.io/#create-order
        """
        signer = self._check_signer(signer)
        return self._post(
            "/orders",
            {
                "parameters": req,
                "signature": signer(
                    sig.create_order_signature_hash(req, self.multiverse_chain, self.sandbox)
                ),
            },
        )

    def create_test_order(
        self, req: request.RestRequestOrder, signer: Optional[sig.MessageSigner] = None
    ) -> response.RestResponseOrder:
        """
        Tests order creation and validation without submitting an order to the matching engine
        See https://api-docs-v3.idex.io/#test-create-order
        """
        signer = self._check_signer(signer)
        return self._post(
            "/orders/test",
            {
                "parameters": req,
                "signature": signer(
                    sig.create_order_signature_hash(req, self.multiverse_chain, self.sandbox)
                ),
            },
        )

    def cancel_order(
        self, req: request.RestRequestCancelOrder, signer: Optional[sig.MessageSigner] = None
    ) -> List[response.RestResponseCanceledOrder]:
        """
        Cancel a single order
        See https://api-docs-v3.idex.io/#cancel-order
        """
        signer = self._check_signer(signer)
        return self._delete(
            "/orders",
            {
                "parameters": req,
                "signature": signer(sig.create_cancel_order_signature_hash(req)),
            },
        )

    def cancel_orders(
        self, req: request.RestRequestCancelOrder, signer: Optional[sig.MessageSigner] = None
    ) -> List[response.RestResponseCanceledOrder]:
        """
        Cancel multiple orders
        See https://api-docs-v3.idex.io/#cancel-order
        """
        signer = self._check_signer(signer)
        return self._delete(
            "/orders",
            {
                "parameters": req,
                "signature": signer(sig.create_cancel_order_signature_hash(req)),
            },
        )

    def get_order(self, req: request.RestRequestFindOrder) -> response.RestResponseOrder:
        """
        Get an order
        See https://api-docs-v3.idex.io/#get-orders
        """
        return self._get("/orders", req)

    def get_orders(self, req: request.RestRequestFindOrders) -> List[response.RestResponseOrder]:
        """
        Get multiple orders
        See https://api-docs-v3.idex.io/#get-orders
        """
        return self._get("/orders", req)

    def get_fill(self, req: request.RestRequestFindFill) -> response.RestResponseFill:
        """
        Get a fill
        See https://api-docs-v3.idex.io/#get-fills
        """
        return self._get("/fills", req)

    def get_fills(self, req: request.RestRequestFindFills) -> List[response.RestResponseFill]:
        """
        Get multiple fills
        See https://api-docs-v3.idex.io/#get-fills
        """
        return self._get("/fills", req)

    # Deposit Endpoints

    def get_deposit(self, req: request.RestRequestFindDeposit) -> response.RestResponseDeposit:
        """
        Get a fill
        See https://api-docs-v3.idex.io/#get-deposits
        """
        return self._get("/deposits", req)

    def get_deposits(
        self, req: request.RestRequestFindDeposits
    ) -> List[response.RestResponseDeposit]:
        """
        Get a fill
        See https://api-docs-v3.idex.io/#get-deposits
        """
        return self._get("/deposits", req)

    # Withdrawal Endpoints

    def withdraw(
        self, req: request.RestRequestWithdrawal, signer: Optional[sig.MessageSigner] = None
    ) -> response.RestResponseWithdrawal:
        """
        Create a new withdrawal
        See https://api-docs-v3.idex.io/#withdraw-funds
        """
        signer = self._check_signer(signer)
        return self._post(
            "/withdrawals",
            {
                "parameters": req,
                "signature": signer(sig.create_withdrawal_signature_hash(req)),
            },
        )

    def get_withdrawal(
        self, req: request.RestRequestFindWithdrawal
    ) -> response.RestResponseWithdrawal:
        """
        Get a withdrawal
        See https://api-docs-v3.idex.io/#get-withdrawals
        """
        return self._get("/withdrawals", req)

    def get_withdrawals(
        self, req: request.RestRequestFindWithdrawals
    ) -> List[response.RestResponseWithdrawal]:
        """
        Get multiple withdrawals
        See https://api-docs-v3.idex.io/#get-withdrawals
        """
        return self._get("/withdrawals", req)

    # WebSocket Authentication Endpoints

    def get_ws_token(self, nonce: str, wallet: str) -> str:
        """
        Get multiple withdrawals
        See https://api-docs-v3.idex.io/#get-withdrawals
        """
        return self._get("/wsToken", {"nonce": nonce, "wallet": wallet})["token"]
