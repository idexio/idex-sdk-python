# <img src="assets/logo.png" alt="IDEX" height="37px" valign="top"> Python SDK

![Discord](https://img.shields.io/discord/455246457465733130?label=Discord&style=flat-square)
![GitHub](https://img.shields.io/github/license/idexio/idex-sdk-js?style=flat-square)
![npm](https://img.shields.io/pypi/v/idex-sdk?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/idexio/idex-sdk-python?style=flat-square)


![Twitter Follow](https://img.shields.io/twitter/follow/idexio?style=social)

The official library for [IDEX v3's](https://idex.io) REST and WebSocket APIs, featuring a real time order book implementation with support for [hybrid liquidity](https://api-docs-v3.idex.io/#hybrid-liquidity).

Complete documentation for the IDEX v3 API is available at https://api-docs-v3.idex.io. 

## Installation

```bash
pip install idex-sdk
```

## Getting Started

- Sign up for [API keys](https://exchange.idex.io/user/signup). Market data endpoints do not require an account.
- A fully-functional [testnet sandbox](https://api-docs-v3.idex.io/#sandbox) is available for development.
- In-depth usage documentation by endpoint is [available here](docs.md).

## Usage Examples

### Public REST API Client

```python
from idex_sdk.client.rest.public import RestPublicClient

c = RestPublicClient()
exchange_info = c.get_exchange_info()
assets = c.get_assets()
markets = c.get_markets()
candles = c.get_candles({"market": "ETH-USDC", "interval": "1h"})
order_book_l2 = c.get_order_book_level2("ETH-USDC")

```

### Authenticated REST API Client

```python
from uuid import uuid1

from idex_sdk.client.rest.authenticated import RestAuthenticatedClient

def uuid() -> str:
    return str(uuid1())

c = RestAuthenticatedClient(
    api_key="<API key>",
    api_secret="<API secret>",
    wallet_private_key="<wallet private key>",
)
wallet_address = "<wallet address>"

get_balances = c.get_balances(
    {
        "nonce": uuid(),
        "wallet": wallet_address,
    }
)

new_order = c.create_order(
    {
        "nonce": uuid(),
        "wallet": wallet_address,
        "market": "ETH-USDC",
        "type": "limit",
        "side": "buy",
        "quantity": "1.00000000",
        "price": "1000.00000000",
    }
)
```

### Real Time Order Book Client

```python
import asyncio

from idex_sdk.client.order_book.real_time import OrderBookRealTimeClient

def update_l2_order_book(market: str) -> None:
    real_time_order_book = client.get_order_book_l2(market, 10)
    print(real_time_order_book)

def make_client() -> OrderBookRealTimeClient:
    client = OrderBookRealTimeClient()
    client.on("l2", update_l2_order_book)
    client.on("ready", update_l2_order_book)
    client.on("error", lambda error: print(f"error {error}"))
    return client

client = make_client()

async def test() -> None:
    task = asyncio.create_task(client.start(["IDEX-USDC"]))
    await task

if __name__ == "__main__":
    asyncio.run(test())
```

## About the Python SDK

This is a python conversion of the [IDEX Typescript SDK](https://github.com/idexio/idex-sdk-js). There is a conversion of all functionality, including typing with `mypy`. There are some small differences in how the `OrderBookRealTimeClient` is run by external code due to differences in how Python's `asyncio` library handles asynchronous code compares to Javascript. See the example code below for more information.


### Setup Repository

- Ensure python3 and [poetry](https://python-poetry.org/docs/) are installed.
- Clone repo
- Cd into repo directory
- Run `poetry install`

The project is now installed to a virtual environment at `./.venv`. Use this environment in the terminal by running `poetry shell`, or by pointing your IDE to it. For example, loading the project directory in VSCode with the Python extension installed should automatically prompt to select the virtual environment.

The project includes configuration (in `pyproject.toml`) for type-checking wih `mypy`, debugging with `debugpy` (for IDEs like neovim), linting with `flake8`, auto-formatting with `black`, and sorting imports with `isort`. If you configure your IDE appropriately, all of this will be automatic. An example VSCode configuration is included.

## Testing
Unit tests are available (using [python unittest](https://docs.python.org/3/library/unittest.html)) for logic-heavy functionality. To run them, run `make test`.

## Generating docs

```
pydoc-markdown -I idex_sdk --render-toc > docs.md
```

## Contract ABIs

Included in the `contracts/` directory contains the ABIs necessary for interacting with IDEX v3's smart contracts.

- The [Exchange ABI](contracts/Exchange.abi.json) can be used to query contract state, [deposit funds](https://api-docs-v3.idex.io/#deposit-funds), [add liquidity](https://api-docs-v3.idex.io/#add-liquidity-via-smart-contract-function-call), [remove liquidity](https://api-docs-v3.idex.io/#remove-liquidity-via-smart-contract-function-call) or [exit wallets](https://api-docs-v3.idex.io/#exit-wallet).
- The [FaucetToken ABI](contracts/FaucetToken.abi.json) is implemented by the [API sandbox](https://api-docs-v3.idex.io/#sandbox) testnet tokens and features a [faucet](https://api-docs-v3.idex.io/#faucets)
function for dispensing tokens.

## License

The IDEX Python SDK is released under the [MIT License](https://opensource.org/licenses/MIT).
