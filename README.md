# idex-sdk-python
This readme is intended for IDEX; there will be some updates needed for publishing, for example the installation instructions will be different when using this project as a published package on pypi versus a local git repository.

This is a python conversion of the [IDEX Typescript SDK](https://github.com/idexio/idex-sdk-js). There is a conversion of all functionality, including typing with `mypy`. There are some small differences in how the `OrderBookRealTimeClient` is run by external code due to differences in how Python's `asyncio` library handles asynchronous code compares to Javascript. See the example code below for more information.


## Setup repository

- Ensure python3 and [poetry](https://python-poetry.org/docs/) are installed.
- Clone repo
- Cd into repo directory
- Run `poetry install`

The project is now installed to a virtual environment at `./.venv`. You can use this environment in the terminal by running `poetry shell`, or by pointing your IDE to it. For example, if you load the project directory in Vscode with the Python extension installed, it should automatically pop up with a prompt to select the virtual environment.

The project includes configuration (in `pyproject.toml`) for type-checking wih `mypy`, debugging with `debugpy` (for IDEs like neovim), linting with `flake8`, auto-formatting with `black`, and sorting imports with `isort`. If you configure your IDE appropriately, all of this will be automatic. See the example vscode config (to be added in `./vscode/settings.json`):

```
{
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true
        }
    },
    "python.testing.unittestArgs": [
        "-v",
        "-s",
        ".",
        "-p",
        "test_*.py"
    ],
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.pytestArgs": [
        "."
    ],
    "python.analysis.diagnosticSeverityOverrides": {
        "reportUndefinedVariable": "none"
    }
}
```

## Testing
There are some unit tests (using [python unittest](https://docs.python.org/3/library/unittest.html)) for logic-heavy functionality in the project. To run them, run `make test`.

## Generating docs

```
pydoc-markdown -I idex_sdk_python --render-toc > docs.md
```

## Example code
RestPublicClient
```
from idex_sdk_python.client.rest.public import RestPublicClient

c = RestPublicClient()
exchange_info = c.get_exchange_info()
assets = c.get_assets()
markets = c.get_markets()
candles = c.get_candles({"market": "ETH-USDC", "interval": "1h"})
order_book_l2 = c.get_order_book_level2("ETH-USDC")
```

RestAuthenticatedClient
```
import os
from uuid import uuid1

from dotenv import load_dotenv

from idex_sdk_python.client.rest.authenticated import RestAuthenticatedClient

load_dotenv()

MATIC_ADDRESS = "0x0000000000000000000000000000000000000000"
USD_ADDRESS = "0x9527D080683C7238E0f78413C18C41491Be73E91"
IDEX_ADDRESS = "0xF8a9D21ad677aB14c33Bf14247e41365C2b70b5d"

def uuid() -> str:
    return str(uuid1())

def format_units(amount: float, decimals: int) -> str:
    return str(int(amount * 10**decimals))

def format_idex(amount: float) -> str:
    return format_units(amount, 18)

def format_usd(amount: float) -> str:
    return format_units(amount, 2)

c = RestAuthenticatedClient(
    api_key=os.getenv("IDEX_API_KEY"),
    api_secret=os.getenv("IDEX_API_SECRET"),
    wallet_private_key=os.getenv("WALLET_PRIVATE_KEY"),
    sandbox=True,
)
wallet_address = os.getenv("WALLET_ADDRESS", "")

get_balances = c.get_balances(
    {
        "nonce": uuid(),
        "wallet": wallet_address,
    }
)

add_liquidity = c.add_liquidity(
    {
        "nonce": uuid(),
        "wallet": wallet_address,
        "tokenA": IDEX_ADDRESS,
        "tokenB": USD_ADDRESS,
        "amountADesired": format_idex(40),
        "amountBDesired": format_usd(20),
        "amountAMin": format_idex(20),
        "amountBMin": format_usd(10),
        "to": wallet_address,
    }
)
```

OrderBookRealTimeClient
```
import asyncio

from idex_sdk_python.client.order_book.real_time import OrderBookRealTimeClient


def ready_callback(market: str) -> None:
    print(f"ready {market}")
    order_book = client.l2_order_books[market]
    print(order_book)


def make_client() -> OrderBookRealTimeClient:
    client = OrderBookRealTimeClient()
    client.on("connected", lambda: print("connected"))
    client.on("disconnected", lambda: print("disconnected"))
    client.on("l1", lambda market: print(f"l1 {market}"))
    client.on("l2", lambda market: print(f"l2 {market}"))
    client.on("ready", ready_callback)
    client.on("error", lambda error: print(f"error {error}"))
    return client


client = make_client()


async def test() -> None:
    global client

    task = asyncio.create_task(client.start(["ETH-USDC"]))
    await task


if __name__ == "__main__":
    asyncio.run(test())
```
