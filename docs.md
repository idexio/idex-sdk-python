# Table of Contents

* [pipmath](#pipmath)
* [constants](#constants)
* [\_\_init\_\_](#__init__)
* [signatures](#signatures)
  * [create\_private\_key\_message\_signer](#signatures.create_private_key_message_signer)
* [idex\_types](#idex_types)
* [idex\_types.websocket.guards](#idex_types.websocket.guards)
* [idex\_types.websocket.constants](#idex_types.websocket.constants)
* [idex\_types.websocket.request](#idex_types.websocket.request)
  * [WebSocketRequestTickersSubscription](#idex_types.websocket.request.WebSocketRequestTickersSubscription)
  * [WebSocketRequestCandlesSubscription](#idex_types.websocket.request.WebSocketRequestCandlesSubscription)
  * [WebSocketRequestTokenPriceSubscription](#idex_types.websocket.request.WebSocketRequestTokenPriceSubscription)
  * [WebSocketRequestTradesSubscription](#idex_types.websocket.request.WebSocketRequestTradesSubscription)
  * [WebSocketRequestL1OrderBookSubscription](#idex_types.websocket.request.WebSocketRequestL1OrderBookSubscription)
  * [WebSocketRequestL2OrderBookSubscription](#idex_types.websocket.request.WebSocketRequestL2OrderBookSubscription)
  * [WebSocketRequestWallet](#idex_types.websocket.request.WebSocketRequestWallet)
* [idex\_types.websocket](#idex_types.websocket)
* [idex\_types.websocket.response](#idex_types.websocket.response)
  * [WebSocketResponseTickerShort](#idex_types.websocket.response.WebSocketResponseTickerShort)
  * [WebSocketResponseCandleShort](#idex_types.websocket.response.WebSocketResponseCandleShort)
  * [WebSocketResponseCandleLong](#idex_types.websocket.response.WebSocketResponseCandleLong)
  * [WebSocketResponseTradeShort](#idex_types.websocket.response.WebSocketResponseTradeShort)
  * [WebSocketResponseLiquidityPoolShort](#idex_types.websocket.response.WebSocketResponseLiquidityPoolShort)
  * [WebSocketResponseLiquidityPoolLong](#idex_types.websocket.response.WebSocketResponseLiquidityPoolLong)
  * [WebSocketResponseL1OrderBookShort](#idex_types.websocket.response.WebSocketResponseL1OrderBookShort)
  * [WebSocketResponseL1OrderBookLong](#idex_types.websocket.response.WebSocketResponseL1OrderBookLong)
  * [WebSocketResponseL2OrderBookShort](#idex_types.websocket.response.WebSocketResponseL2OrderBookShort)
  * [WebSocketResponseL2OrderBookLong](#idex_types.websocket.response.WebSocketResponseL2OrderBookLong)
  * [WebSocketResponseBalanceShort](#idex_types.websocket.response.WebSocketResponseBalanceShort)
  * [WebSocketResponseBalanceLong](#idex_types.websocket.response.WebSocketResponseBalanceLong)
  * [WebSocketResponseOrderFillShort](#idex_types.websocket.response.WebSocketResponseOrderFillShort)
  * [WebSocketResponseOrderShort](#idex_types.websocket.response.WebSocketResponseOrderShort)
  * [WebSocketResponseOrderLong](#idex_types.websocket.response.WebSocketResponseOrderLong)
  * [WebSocketResponseTokenPriceShort](#idex_types.websocket.response.WebSocketResponseTokenPriceShort)
  * [WebSocketResponseTokenPriceLong](#idex_types.websocket.response.WebSocketResponseTokenPriceLong)
  * [WebSocketResponseError](#idex_types.websocket.response.WebSocketResponseError)
  * [WebSocketResponseSubscriptions](#idex_types.websocket.response.WebSocketResponseSubscriptions)
* [idex\_types.enums](#idex_types.enums)
* [idex\_types.order\_book](#idex_types.order_book)
  * [OrderBookFeesAndMinimums](#idex_types.order_book.OrderBookFeesAndMinimums)
* [idex\_types.errors](#idex_types.errors)
* [idex\_types.rest.guards](#idex_types.rest.guards)
* [idex\_types.rest.request](#idex_types.rest.request)
  * [RestRequestFindLiquidityPools](#idex_types.rest.request.RestRequestFindLiquidityPools)
  * [RestRequestAddLiquidity](#idex_types.rest.request.RestRequestAddLiquidity)
  * [RestRequestRemoveLiquidity](#idex_types.rest.request.RestRequestRemoveLiquidity)
  * [RestRequestFindLiquidityAddition](#idex_types.rest.request.RestRequestFindLiquidityAddition)
  * [RestRequestFindLiquidityRemoval](#idex_types.rest.request.RestRequestFindLiquidityRemoval)
  * [RestRequestFindLiquidityChanges](#idex_types.rest.request.RestRequestFindLiquidityChanges)
  * [RestRequestCancelOrders](#idex_types.rest.request.RestRequestCancelOrders)
  * [RestRequestFindBalances](#idex_types.rest.request.RestRequestFindBalances)
  * [RestRequestFindCandles](#idex_types.rest.request.RestRequestFindCandles)
  * [RestRequestFindDeposit](#idex_types.rest.request.RestRequestFindDeposit)
  * [RestRequestFindDeposits](#idex_types.rest.request.RestRequestFindDeposits)
  * [RestRequestFindFill](#idex_types.rest.request.RestRequestFindFill)
  * [RestRequestFindFills](#idex_types.rest.request.RestRequestFindFills)
  * [RestRequestFindMarkets](#idex_types.rest.request.RestRequestFindMarkets)
  * [RestRequestFindOrder](#idex_types.rest.request.RestRequestFindOrder)
  * [RestRequestFindOrders](#idex_types.rest.request.RestRequestFindOrders)
  * [RestRequestFindTrades](#idex_types.rest.request.RestRequestFindTrades)
  * [RestRequestFindWithdrawal](#idex_types.rest.request.RestRequestFindWithdrawal)
  * [RestRequestFindWithdrawals](#idex_types.rest.request.RestRequestFindWithdrawals)
  * [RestRequestAssociateWallet](#idex_types.rest.request.RestRequestAssociateWallet)
* [idex\_types.rest](#idex_types.rest)
* [idex\_types.rest.response](#idex_types.rest.response)
  * [RestResponseBalance](#idex_types.rest.response.RestResponseBalance)
  * [RestResponseCandle](#idex_types.rest.response.RestResponseCandle)
  * [RestResponseDeposit](#idex_types.rest.response.RestResponseDeposit)
  * [RestResponseExchangeInfo](#idex_types.rest.response.RestResponseExchangeInfo)
  * [RestResponseOrderFill](#idex_types.rest.response.RestResponseOrderFill)
  * [RestResponseFill](#idex_types.rest.response.RestResponseFill)
  * [RestResponseLiquidityPool](#idex_types.rest.response.RestResponseLiquidityPool)
  * [RestResponseLiquidityAddition](#idex_types.rest.response.RestResponseLiquidityAddition)
  * [RestResponseLiquidityPoolReserves](#idex_types.rest.response.RestResponseLiquidityPoolReserves)
  * [RestResponseLiquidityRemoval](#idex_types.rest.response.RestResponseLiquidityRemoval)
  * [RestResponseMarket](#idex_types.rest.response.RestResponseMarket)
  * [RestResponseOrder](#idex_types.rest.response.RestResponseOrder)
  * [RestResponseTicker](#idex_types.rest.response.RestResponseTicker)
  * [RestResponseTrade](#idex_types.rest.response.RestResponseTrade)
  * [RestResponseUser](#idex_types.rest.response.RestResponseUser)
  * [RestResponseWallet](#idex_types.rest.response.RestResponseWallet)
  * [RestResponseWithdrawal](#idex_types.rest.response.RestResponseWithdrawal)
  * [RestResponseAssociateWallet](#idex_types.rest.response.RestResponseAssociateWallet)
* [order\_book](#order_book)
* [order\_book.api\_conversions](#order_book.api_conversions)
* [order\_book.hybrid](#order_book.hybrid)
  * [l2\_limit\_order\_book\_to\_hybrid\_order\_books](#order_book.hybrid.l2_limit_order_book_to_hybrid_order_books)
* [order\_book.quantities](#order_book.quantities)
  * [calculate\_gross\_base\_quantity](#order_book.quantities.calculate_gross_base_quantity)
  * [calculate\_gross\_base\_value\_of\_buy\_quantities](#order_book.quantities.calculate_gross_base_value_of_buy_quantities)
  * [calculate\_gross\_quote\_quantity](#order_book.quantities.calculate_gross_quote_quantity)
  * [calculate\_gross\_quote\_value\_of\_sell\_quantities](#order_book.quantities.calculate_gross_quote_value_of_sell_quantities)
  * [calculate\_base\_quantity\_out](#order_book.quantities.calculate_base_quantity_out)
  * [calculate\_quote\_quantity\_out](#order_book.quantities.calculate_quote_quantity_out)
  * [calculate\_synthetic\_price\_levels](#order_book.quantities.calculate_synthetic_price_levels)
  * [recalculate\_hybrid\_level\_amounts](#order_book.quantities.recalculate_hybrid_level_amounts)
  * [sort\_and\_merge\_levels\_unadjusted](#order_book.quantities.sort_and_merge_levels_unadjusted)
  * [quantities\_available\_from\_pool\_at\_ask\_price](#order_book.quantities.quantities_available_from_pool_at_ask_price)
  * [quantities\_available\_from\_pool\_at\_bid\_price](#order_book.quantities.quantities_available_from_pool_at_bid_price)
  * [aggregate\_l2\_order\_book\_at\_tick\_size](#order_book.quantities.aggregate_l2_order_book_at_tick_size)
  * [l1\_or\_l2\_best\_available\_prices](#order_book.quantities.l1_or_l2_best_available_prices)
  * [l1\_l2\_order\_books\_with\_minimum\_taker](#order_book.quantities.l1_l2_order_books_with_minimum_taker)
  * [validate\_synthetic\_price\_level\_inputs](#order_book.quantities.validate_synthetic_price_level_inputs)
  * [adjust\_price\_to\_tick\_size](#order_book.quantities.adjust_price_to_tick_size)
* [order\_book.utils](#order_book.utils)
  * [l2\_to\_l1\_order\_book](#order_book.utils.l2_to_l1_order_book)
* [client](#client)
* [client.websocket.client](#client.websocket.client)
  * [WebSocketClient](#client.websocket.client.WebSocketClient)
    * [\_\_init\_\_](#client.websocket.client.WebSocketClient.__init__)
    * [connect](#client.websocket.client.WebSocketClient.connect)
    * [subscribe\_authenticated](#client.websocket.client.WebSocketClient.subscribe_authenticated)
    * [subscribe\_unauthenticated](#client.websocket.client.WebSocketClient.subscribe_unauthenticated)
    * [subscribe](#client.websocket.client.WebSocketClient.subscribe)
    * [reconnect](#client.websocket.client.WebSocketClient.reconnect)
* [client.websocket](#client.websocket)
* [client.websocket.utils](#client.websocket.utils)
* [client.websocket.transform](#client.websocket.transform)
* [client.utils](#client.utils)
* [client.order\_book](#client.order_book)
* [client.order\_book.real\_time](#client.order_book.real_time)
  * [OrderBookRealTimeClient](#client.order_book.real_time.OrderBookRealTimeClient)
    * [start](#client.order_book.real_time.OrderBookRealTimeClient.start)
    * [stop](#client.order_book.real_time.OrderBookRealTimeClient.stop)
    * [set\_fees\_and\_minimums\_override](#client.order_book.real_time.OrderBookRealTimeClient.set_fees_and_minimums_override)
    * [get\_order\_book\_l1](#client.order_book.real_time.OrderBookRealTimeClient.get_order_book_l1)
    * [get\_order\_book\_l2](#client.order_book.real_time.OrderBookRealTimeClient.get_order_book_l2)
* [client.order\_book.utils](#client.order_book.utils)
  * [l1\_equal](#client.order_book.utils.l1_equal)
  * [update\_l2\_side](#client.order_book.utils.update_l2_side)
  * [update\_l2\_levels](#client.order_book.utils.update_l2_levels)
* [client.rest.public](#client.rest.public)
  * [RestPublicClient](#client.rest.public.RestPublicClient)
    * [ping](#client.rest.public.RestPublicClient.ping)
    * [get\_server\_time](#client.rest.public.RestPublicClient.get_server_time)
    * [get\_exchange\_info](#client.rest.public.RestPublicClient.get_exchange_info)
    * [get\_assets](#client.rest.public.RestPublicClient.get_assets)
    * [get\_markets](#client.rest.public.RestPublicClient.get_markets)
    * [get\_liquidity\_pools](#client.rest.public.RestPublicClient.get_liquidity_pools)
    * [get\_tickers](#client.rest.public.RestPublicClient.get_tickers)
    * [get\_candles](#client.rest.public.RestPublicClient.get_candles)
    * [get\_trades](#client.rest.public.RestPublicClient.get_trades)
    * [get\_order\_book\_level1](#client.rest.public.RestPublicClient.get_order_book_level1)
    * [get\_order\_book\_level2](#client.rest.public.RestPublicClient.get_order_book_level2)
* [client.rest](#client.rest)
* [client.rest.authenticated](#client.rest.authenticated)
  * [RestAuthenticatedClient](#client.rest.authenticated.RestAuthenticatedClient)
    * [add\_liquidity](#client.rest.authenticated.RestAuthenticatedClient.add_liquidity)
    * [remove\_liquidity](#client.rest.authenticated.RestAuthenticatedClient.remove_liquidity)
    * [get\_liquidity\_addition](#client.rest.authenticated.RestAuthenticatedClient.get_liquidity_addition)
    * [get\_liquidity\_additions](#client.rest.authenticated.RestAuthenticatedClient.get_liquidity_additions)
    * [get\_liquidity\_removal](#client.rest.authenticated.RestAuthenticatedClient.get_liquidity_removal)
    * [get\_liquidity\_removals](#client.rest.authenticated.RestAuthenticatedClient.get_liquidity_removals)
    * [get\_user](#client.rest.authenticated.RestAuthenticatedClient.get_user)
    * [get\_wallets](#client.rest.authenticated.RestAuthenticatedClient.get_wallets)
    * [get\_balances](#client.rest.authenticated.RestAuthenticatedClient.get_balances)
    * [associate\_wallet](#client.rest.authenticated.RestAuthenticatedClient.associate_wallet)
    * [create\_order](#client.rest.authenticated.RestAuthenticatedClient.create_order)
    * [create\_test\_order](#client.rest.authenticated.RestAuthenticatedClient.create_test_order)
    * [cancel\_order](#client.rest.authenticated.RestAuthenticatedClient.cancel_order)
    * [cancel\_orders](#client.rest.authenticated.RestAuthenticatedClient.cancel_orders)
    * [get\_order](#client.rest.authenticated.RestAuthenticatedClient.get_order)
    * [get\_orders](#client.rest.authenticated.RestAuthenticatedClient.get_orders)
    * [get\_fill](#client.rest.authenticated.RestAuthenticatedClient.get_fill)
    * [get\_fills](#client.rest.authenticated.RestAuthenticatedClient.get_fills)
    * [get\_deposit](#client.rest.authenticated.RestAuthenticatedClient.get_deposit)
    * [get\_deposits](#client.rest.authenticated.RestAuthenticatedClient.get_deposits)
    * [withdraw](#client.rest.authenticated.RestAuthenticatedClient.withdraw)
    * [get\_withdrawal](#client.rest.authenticated.RestAuthenticatedClient.get_withdrawal)
    * [get\_withdrawals](#client.rest.authenticated.RestAuthenticatedClient.get_withdrawals)
    * [get\_ws\_token](#client.rest.authenticated.RestAuthenticatedClient.get_ws_token)

<a id="pipmath"></a>

# pipmath

<a id="constants"></a>

# constants

<a id="__init__"></a>

# \_\_init\_\_

<a id="signatures"></a>

# signatures

<a id="signatures.create_private_key_message_signer"></a>

#### create\_private\_key\_message\_signer

```python
def create_private_key_message_signer(
        wallet_private_key: str) -> MessageSigner
```

Returns a function which signs a message with the originally provided private key.

**Arguments**:

- `wallet_private_key` - Private key to use when signing messages
  

**Returns**:

  The message signing function

<a id="idex_types"></a>

# idex\_types

<a id="idex_types.websocket.guards"></a>

# idex\_types.websocket.guards

<a id="idex_types.websocket.constants"></a>

# idex\_types.websocket.constants

<a id="idex_types.websocket.request"></a>

# idex\_types.websocket.request

<a id="idex_types.websocket.request.WebSocketRequestTickersSubscription"></a>

## WebSocketRequestTickersSubscription Objects

```python
class WebSocketRequestTickersSubscription(TypedDict)
```

Tickers subscription

**Attributes**:

- `name` - 'tickers'
- `markets` - array of market symbols

<a id="idex_types.websocket.request.WebSocketRequestCandlesSubscription"></a>

## WebSocketRequestCandlesSubscription Objects

```python
class WebSocketRequestCandlesSubscription(TypedDict)
```

Candles subscription

**Attributes**:

- `name` - 'candles'
- `markets` - array of market symbols
- `interval` - candle interval

<a id="idex_types.websocket.request.WebSocketRequestTokenPriceSubscription"></a>

## WebSocketRequestTokenPriceSubscription Objects

```python
class WebSocketRequestTokenPriceSubscription(TypedDict)
```

Token price subscription

**Attributes**:

- `name` - 'tokenprice'
- `markets` - array of market symbols

<a id="idex_types.websocket.request.WebSocketRequestTradesSubscription"></a>

## WebSocketRequestTradesSubscription Objects

```python
class WebSocketRequestTradesSubscription(TypedDict)
```

Trades subscription

**Attributes**:

- `name` - 'trades'
- `markets` - array of market symbols

<a id="idex_types.websocket.request.WebSocketRequestL1OrderBookSubscription"></a>

## WebSocketRequestL1OrderBookSubscription Objects

```python
class WebSocketRequestL1OrderBookSubscription(TypedDict)
```

L1 order book subscription

**Attributes**:

- `name` - 'l1orderbook'
- `markets` - array of market symbols

<a id="idex_types.websocket.request.WebSocketRequestL2OrderBookSubscription"></a>

## WebSocketRequestL2OrderBookSubscription Objects

```python
class WebSocketRequestL2OrderBookSubscription(TypedDict)
```

L2 order book subscription

**Attributes**:

- `name` - 'l2orderbook'
- `markets` - array of market symbols

<a id="idex_types.websocket.request.WebSocketRequestWallet"></a>

## WebSocketRequestWallet Objects

```python
class WebSocketRequestWallet(TypedDict)
```

wallet is required and is only handled by the idex-sdk.
It is used to auto generate the required wsToken

<a id="idex_types.websocket"></a>

# idex\_types.websocket

<a id="idex_types.websocket.response"></a>

# idex\_types.websocket.response

<a id="idex_types.websocket.response.WebSocketResponseTickerShort"></a>

## WebSocketResponseTickerShort Objects

```python
class WebSocketResponseTickerShort(TypedDict)
```

**Attributes**:

- `m` - (market) Market symbol
- `t` - (time) Timestamp when the statistics were computed, the opening time of the period is
  24 hours prior
- `o` - (open) Price of the first trade in the period in quote terms
- `h` - (high) Highest traded price in the period in quote terms
- `l` - (low) Lowest traded price in the period in quote terms
- `c` - (close) Price of the last trade in the period in quote terms
- `Q` - (closeQuantity) Quantity of the last trade in th period in base terms
- `v` - (baseVolume) Trailing 24-hour trading volume in base terms
- `q` - (quoteVolume) Trailing 24-hour trading volume in quote terms
- `P` - (percentChange) Percentage change from open price to close price
- `n` - (numTrades) Number of trades in the period
- `a` - (ask) Best ask price on the order book in quote terms
- `b` - (bid) Best bid price on the order book in quote terms
- `u` - (sequence) Fill sequence number of the last trade in the period

<a id="idex_types.websocket.response.WebSocketResponseCandleShort"></a>

## WebSocketResponseCandleShort Objects

```python
class WebSocketResponseCandleShort(TypedDict)
```

**Attributes**:

- `m` - (market) Market symbol
- `t` - (time) Timestamp when the statistics were computed, time is always between the start
  and end timestamps of the interval
- `i` - (interval) Interval duration, see Interval Values
- `s` - (start) Timestamp of the start of the interval
- `e` - (end) Timestamp of the end of the interval
- `o` - (open) Price of the first trade in the interval in quote terms
- `h` - (high) Highest traded price in the interval in quote terms
- `l` - (low) Lowest traded price in the interval in quote terms
- `c` - (close) Price of the last trade in the interval in quote terms
- `v` - (volume) Trading volume in the interval in base terms
- `n` - (numTrades) Number of trades in the candle
- `u` - (sequence) Fill sequence number of the last trade in the interval

<a id="idex_types.websocket.response.WebSocketResponseCandleLong"></a>

## WebSocketResponseCandleLong Objects

```python
class WebSocketResponseCandleLong(rest_response.RestResponseCandle)
```

**Attributes**:

- `market` - Market symbol
- `time` - Timestamp when the statistics were computed, time is always between the start and
  end timestamps of the interval
- `interval` - Interval duration, see Interval Values
- `start` - Timestamp of the start of the interval
- `end` - Timestamp of the end of the interval
- `open` - Price of the first trade in the interval in quote terms
- `high` - Highest traded price in the interval in quote terms
- `low` - Lowest traded price in the interval in quote terms
- `close` - Price of the last trade in the interval in quote terms
- `volume` - Trading volume in the interval in base terms
- `numTrades` - Number of trades in the candle
- `sequence` - Fill sequence number of the last trade in the interval

<a id="idex_types.websocket.response.WebSocketResponseTradeShort"></a>

## WebSocketResponseTradeShort Objects

```python
class WebSocketResponseTradeShort(TypedDict)
```

**Attributes**:

- `y` - (type) orderBook, pool, or hybrid
- `m` - (market) Market symbol
- `i` - (fillId) Trade identifier
- `p` - (price) Price of the trade in quote terms
- `q` - (quantity) Quantity of the trade in base terms
- `Q` - (quoteQuantity) Quantity of the trade in quote terms
- `t` - (time) Timestamp of the trade
- `s` - (makerSide) Maker side of the trade, buy or sell
- `u` - (sequence) Fill sequence number of the trade

<a id="idex_types.websocket.response.WebSocketResponseLiquidityPoolShort"></a>

## WebSocketResponseLiquidityPoolShort Objects

```python
class WebSocketResponseLiquidityPoolShort(TypedDict)
```

**Attributes**:

- `q` - (baseReserveQuantity) quantity of base asset held in the liquidity pool
- `Q` - (quoteReserveQuantity) quantity of quote asset held in the liquidity pool

<a id="idex_types.websocket.response.WebSocketResponseLiquidityPoolLong"></a>

## WebSocketResponseLiquidityPoolLong Objects

```python
class WebSocketResponseLiquidityPoolLong(TypedDict)
```

**Attributes**:

- `baseReserveQuantity` - quantity of base asset held in the liquidity pool
- `quoteReserveQuantity` - quantity of quote asset held in the liquidity pool

<a id="idex_types.websocket.response.WebSocketResponseL1OrderBookShort"></a>

## WebSocketResponseL1OrderBookShort Objects

```python
class WebSocketResponseL1OrderBookShort(TypedDict)
```

**Attributes**:

- `m` - (market) Market symbol
- `t` - (time) Timestamp of the order book update
- `b` - (bidPrice) Best bid price
- `B` - (bidQuantity) Quantity available at the best bid price
- `a` - (askPrice) Best ask price
- `A` - (askQuantity) Quantity available at the best ask price
- `p` - Liquidity pool reserves for this market

<a id="idex_types.websocket.response.WebSocketResponseL1OrderBookLong"></a>

## WebSocketResponseL1OrderBookLong Objects

```python
class WebSocketResponseL1OrderBookLong(TypedDict)
```

**Attributes**:

- `market` - Market symbol
- `time` - Timestamp of the order book update
- `bidPrice` - Best bid price
- `bidQuantity` - Quantity available at the best bid price
- `askPrice` - Best ask price
- `askQuantity` - Quantity available at the best ask price
- `pool` - Liquidity pool reserves for this market

<a id="idex_types.websocket.response.WebSocketResponseL2OrderBookShort"></a>

## WebSocketResponseL2OrderBookShort Objects

```python
class WebSocketResponseL2OrderBookShort(TypedDict)
```

**Attributes**:

- `m` - (market) Market symbol
- `t` - (time) Timestamp of the order book update
- `u` - (sequence) Order book update sequence number of the update
- `b` - (bids) Array of bid price level updates
- `a` - (asks) Array of ask price level updates
- `p` - Liquidity pool reserves for this market

<a id="idex_types.websocket.response.WebSocketResponseL2OrderBookLong"></a>

## WebSocketResponseL2OrderBookLong Objects

```python
class WebSocketResponseL2OrderBookLong(TypedDict)
```

**Attributes**:

- `market` - Market symbol
- `time` - Timestamp of the order book update
- `sequence` - Order book update sequence number of the update
- `bids` - Array of bid price level updates
- `asks` - Array of ask price level updates
- `pool` - liquidity pool reserves
- `p` - Liquidity pool reserves for this market

<a id="idex_types.websocket.response.WebSocketResponseBalanceShort"></a>

## WebSocketResponseBalanceShort Objects

```python
class WebSocketResponseBalanceShort(TypedDict)
```

**Attributes**:

- `w` - (wallet) Target wallet address
- `a` - (asset) Asset symbol
- `q` - (quantity) Total quantity of the asset held by the wallet on the exchange
- `f` - (availableForTrade) Quantity of the asset available for trading; quantity: locked
- `l` - (locked) Quantity of the asset held in trades on the order book
- `d` - (usdValue) Total value of the asset held by the wallet on the exchange in USD

<a id="idex_types.websocket.response.WebSocketResponseBalanceLong"></a>

## WebSocketResponseBalanceLong Objects

```python
class WebSocketResponseBalanceLong(TypedDict)
```

**Attributes**:

- `wallet` - Target wallet address
- `asset` - Asset symbol
- `quantity` - Total quantity of the asset held by the wallet on the exchange
- `availableForTrade` - Quantity of the asset available for trading; quantity: locked
- `locked` - Quantity of the asset held in trades on the order book
- `usdValue` - Total value of the asset held by the wallet on the exchange in USD

<a id="idex_types.websocket.response.WebSocketResponseOrderFillShort"></a>

## WebSocketResponseOrderFillShort Objects

```python
class WebSocketResponseOrderFillShort(
        _WebSocketResponseOrderFillShortRequiredAttribs)
```

**Attributes**:

- `i` - (fillId) Fill identifier
- `p` - (price) Price of the fill in quote terms
- `q` - (quantity) Quantity of the fill in base terms
- `Q` - (quoteQuantity) Quantity of the fill in quote terms
- `oq` - Quantity of the fill in base terms supplied by order book liquidity, omitted
  for pool fills
- `oQ` - Quantity of the fill in quote terms supplied by order book liquidity, omitted
  for pool fills
- `pq` - Quantity of the fill in base terms supplied by pool liquidity, omitted
  for orderBook fills
- `pQ` - Quantity of the fill in quote terms supplied by pool liquidity, omitted
  for orderBook fills
- `t` - (time) Timestamp of the fill
- `s` - (makerSide) Maker side of the fill, buy or sell
- `u` - (sequence) Fill sequence number
- `f` - (fee) Fee amount collected on the fill
- `a` - (feeAsset) Symbol of asset in which fees collected
- `g` - (gas) Amount collected to cover trade settlement gas costs, only present for taker
- `l` - (liquidity) Whether the fill is the maker or taker in the trade from the perspective of
  the requesting user account, maker or taker
- `T` - (txId) Ethereum ID of the trade settlement transaction
- `S` - (txStatus) Status of the trade settlement transaction, see values

<a id="idex_types.websocket.response.WebSocketResponseOrderShort"></a>

## WebSocketResponseOrderShort Objects

```python
class WebSocketResponseOrderShort(_WebSocketResponseOrderShortRequiredAttribs)
```

**Attributes**:

- `m` - (market) Market symbol
- `i` - (orderId) Exchange-assigned order identifier
- `c` - (clientOrderId) Client-specified order identifier
  w : (wallet) Ethereum address of placing wallet
- `t` - (executionTime) Timestamp of the most recent update
- `T` - (time) Timestamp of initial order processing by the matching engine
- `x` - (update) Type of order update, see values
- `X` - (status) Order status, see values
- `u` - (sequence) order book update sequence number, only included if update type triggers an
  order book update
- `o` - (type) Order type, see values
- `S` - (side) Order side, buy or sell
- `q` - (originalQuantity) Original quantity specified by the order in base terms, omitted for
  market orders specified in quote terms
- `Q` - (originalQuoteQuantity) Original quantity specified by the order in quote terms, only
  present for market orders specified in quote term
- `z` - (executedQuantity) Quantity that has been executed in base terms
- `Z` - (cumulativeQuoteQuantity) Cumulative quantity that has been spent (buy orders) or
  received (sell orders) in quote terms, omitted if unavailable for historical orders
- `v` - (avgExecutionPrice) Weighted average price of fills associated with the order; only
  present with fills
- `p` - (price) Original price specified by the order in quote terms, omitted for all market
  orders
- `P` - (stopPrice) Stop loss or take profit price, only present for stopLoss, stopLossLimit,
  takeProfit, and takeProfitLimit orders
- `f` - (timeInForce) Time in force policy, see values, only present for limit orders
- `V` - (selfTradePrevention) Self-trade prevention policy, see values
- `F` - (fills) Array of order fill objects

<a id="idex_types.websocket.response.WebSocketResponseOrderLong"></a>

## WebSocketResponseOrderLong Objects

```python
class WebSocketResponseOrderLong(_WebSocketResponseOrderLongRequiredAttribs)
```

**Attributes**:

- `market` - Market symbol
- `orderId` - Exchange-assigned order identifier
- `clientOrderId` - Client-specified order identifier
- `wallet` - Ethereum address of placing wallet
- `executionTime` - Timestamp of the most recent update
- `time` - Timestamp of initial order processing by the matching engine
- `update` - Type of order update, see values
- `status` - Order status, see values
- `sequence` - order book update sequence number, only included if update type triggers
  an order book update
- `type` - Order type, see values
- `side` - Order side, buy or sell
- `originalQuantity` - Original quantity specified by the order in base terms, omitted for
  market orders specified in quote terms
- `originalQuoteQuantity` - Original quantity specified by the order in quote terms, only
  present for market orders specified in quote terms
- `executedQuantity` - Quantity that has been executed in base terms
- `cumulativeQuoteQuantity` - Cumulative quantity that has been spent (buy orders) or received
  (sell orders) in quote terms, omitted if unavailable for historical orders
- `avgExecutionPrice` - Weighted average price of fills associated with the order; only present
  with fills
- `price` - Original price specified by the order in quote terms, omitted for all market orders
- `stopPrice` - Stop loss or take profit price, only present for stopLoss, stopLossLimit,
  takeProfit, and takeProfitLimit orders
- `timeInForce` - Time in force policy, see values, only present for limit orders
- `selfTradePrevention` - Self-trade prevention policy, see values
- `fills` - Array of order fill objects

<a id="idex_types.websocket.response.WebSocketResponseTokenPriceShort"></a>

## WebSocketResponseTokenPriceShort Objects

```python
class WebSocketResponseTokenPriceShort(TypedDict)
```

**Attributes**:

- `t` - (token) Token symbol
- `p` - (price) Current price of token relative to the native asset

<a id="idex_types.websocket.response.WebSocketResponseTokenPriceLong"></a>

## WebSocketResponseTokenPriceLong Objects

```python
class WebSocketResponseTokenPriceLong(TypedDict)
```

**Attributes**:

- `token` - Token symbol
- `price` - Current price of token relative to the native asset

<a id="idex_types.websocket.response.WebSocketResponseError"></a>

## WebSocketResponseError Objects

```python
class WebSocketResponseError(_WebSocketResponseErrorRequiredAttribs)
```

Error response

**Attributes**:

  cid
  error
  data
- `data.code` - error short code
- `data.message` - human readable error message

<a id="idex_types.websocket.response.WebSocketResponseSubscriptions"></a>

## WebSocketResponseSubscriptions Objects

```python
class WebSocketResponseSubscriptions(
        _WebSocketResponseSubscriptionsRequiredAttribs)
```

Subscriptions response

**Attributes**:

  cid
- `type` - subscriptions
  subscriptions
- `Subscription.name` - subscription name
- `Subscription.markets` - markets
- `Subscription.interval` - candle interval
- `Subscription.wallet` - wallet address

<a id="idex_types.enums"></a>

# idex\_types.enums

<a id="idex_types.order_book"></a>

# idex\_types.order\_book

<a id="idex_types.order_book.OrderBookFeesAndMinimums"></a>

## OrderBookFeesAndMinimums Objects

```python
class OrderBookFeesAndMinimums(TypedDict)
```

**Attributes**:

- `takerIdexFeeRate` - Taker trade fee rate collected by IDEX; used in computing synthetic
  price levels for real-time order book
- `takerLiquidityProviderFeeRate` - Taker trade fee rate collected by liquidity providers; used
  in computing synthetic price levels for real-time order book
- `takerTradeMinimum` - Minimum order size that is accepted by the matching engine for
  execution in MATIC, applies to both MATIC and token

<a id="idex_types.errors"></a>

# idex\_types.errors

<a id="idex_types.rest.guards"></a>

# idex\_types.rest.guards

<a id="idex_types.rest.request"></a>

# idex\_types.rest.request

<a id="idex_types.rest.request.RestRequestFindLiquidityPools"></a>

## RestRequestFindLiquidityPools Objects

```python
class RestRequestFindLiquidityPools(TypedDict)
```

**Attributes**:

- `market` - Target market
- `tokenA` - Address of one reserve token
- `tokenB` - Address of one reserve token

<a id="idex_types.rest.request.RestRequestAddLiquidity"></a>

## RestRequestAddLiquidity Objects

```python
class RestRequestAddLiquidity(TypedDict)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `tokenA` - Asset by address
- `tokenB` - Asset by address
- `amountADesired` - Maximum amount of tokenA to add to the liquidity pool
- `amountBDesired` - Maximum amount of tokenB to add to the liquidity pool
- `amountAMin` - Minimum amount of tokenA to add to the liquidity pool
- `amountBMin` - Minimum amount of tokenB to add to the liquidity pool
- `to` - Wallet to credit LP tokens, or the custodian contract address to leave on exchange

<a id="idex_types.rest.request.RestRequestRemoveLiquidity"></a>

## RestRequestRemoveLiquidity Objects

```python
class RestRequestRemoveLiquidity(TypedDict)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `tokenA` - Asset by address
- `tokenB` - Asset by address
- `liquidity` - LP tokens to burn
- `amountAMin` - Minimum amount of tokenA to add to the liquidity pool
- `amountBMin` - Minimum amount of tokenB to add to the liquidity pool
- `to` - Wallet to credit LP tokens, or the custodian contract address to leave on exchange

<a id="idex_types.rest.request.RestRequestFindLiquidityAddition"></a>

## RestRequestFindLiquidityAddition Objects

```python
class RestRequestFindLiquidityAddition(RestRequestFindLiquidityChange,
                                       RestRequestFindWithPagination)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `liquidityAdditionId` - Single liquidityAdditionId to return; exclusive with initiatingTxId
- `initiatingTxId` - Transaction id of the Exchange contract addLiquidity or addLiquidityETH
  call transaction, only applies to chain-initiated liquidity additions; exclusive
  with liquidityAdditionId
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Liquidity additions created at the same timestamp or after fromId

<a id="idex_types.rest.request.RestRequestFindLiquidityRemoval"></a>

## RestRequestFindLiquidityRemoval Objects

```python
class RestRequestFindLiquidityRemoval(RestRequestFindLiquidityChange,
                                      RestRequestFindWithPagination)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `liquidityRemovalId` - Single liquidityRemovalId to return; exclusive with initiatingTxId
- `initiatingTxId` - Transaction id of the Exchange contract removeLiquidity or
  removeLiquidityETH call transaction, only applies to chain-initiated liquidity
  removals; exclusive with liquidityRemovalId
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Liquidity additions created at the same timestamp or after fromId

<a id="idex_types.rest.request.RestRequestFindLiquidityChanges"></a>

## RestRequestFindLiquidityChanges Objects

```python
class RestRequestFindLiquidityChanges(
        _RestRequestFindLiquidityChangesRequiredAttribs)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Deposits created at the same timestamp or after fromId

<a id="idex_types.rest.request.RestRequestCancelOrders"></a>

## RestRequestCancelOrders Objects

```python
class RestRequestCancelOrders(RestRequestCancelOrdersBase)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `market` - Base-quote pair e.g. 'IDEX-ETH'

<a id="idex_types.rest.request.RestRequestFindBalances"></a>

## RestRequestFindBalances Objects

```python
class RestRequestFindBalances(RestRequestFindByWallet)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `assets` - Asset symbols

<a id="idex_types.rest.request.RestRequestFindCandles"></a>

## RestRequestFindCandles Objects

```python
class RestRequestFindCandles(RestRequestFindWithPagination)
```

**Attributes**:

- `market` - Base-quote pair e.g. 'IDEX-ETH'
- `interval` - Time interval for data
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000

<a id="idex_types.rest.request.RestRequestFindDeposit"></a>

## RestRequestFindDeposit Objects

```python
class RestRequestFindDeposit(RestRequestFindByWallet)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
  depositId

<a id="idex_types.rest.request.RestRequestFindDeposits"></a>

## RestRequestFindDeposits Objects

```python
class RestRequestFindDeposits(RestRequestFindByWallet,
                              RestRequestFindWithPagination)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
- `asset` - Asset by symbol
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Deposits created at the same timestamp or after fromId

<a id="idex_types.rest.request.RestRequestFindFill"></a>

## RestRequestFindFill Objects

```python
class RestRequestFindFill(RestRequestFindByWallet)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
  fillId

<a id="idex_types.rest.request.RestRequestFindFills"></a>

## RestRequestFindFills Objects

```python
class RestRequestFindFills(RestRequestFindByWallet,
                           RestRequestFindWithPagination)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - Ethereum wallet address
- `market` - Base-quote pair e.g. 'IDEX-ETH'
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Fills created at the same timestamp or after fillId

<a id="idex_types.rest.request.RestRequestFindMarkets"></a>

## RestRequestFindMarkets Objects

```python
class RestRequestFindMarkets(TypedDict)
```

**Attributes**:

- `market` - Target market, all markets are returned if omitted

<a id="idex_types.rest.request.RestRequestFindOrder"></a>

## RestRequestFindOrder Objects

```python
class RestRequestFindOrder(RestRequestFindByWallet)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
- `orderId` - Single orderId or clientOrderId to cancel; prefix client-provided ids with client

<a id="idex_types.rest.request.RestRequestFindOrders"></a>

## RestRequestFindOrders Objects

```python
class RestRequestFindOrders(RestRequestFindByWallet,
                            RestRequestFindWithPagination)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
- `market` - Base-quote pair e.g. 'IDEX-ETH'
- `closed` - false only returns active orders on the order book; true only returns orders that
  are no longer on the order book and resulted in at least one fill; only applies if
  orderId is absent
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - order_id of the earliest (oldest) order, only applies if orderId is absent

<a id="idex_types.rest.request.RestRequestFindTrades"></a>

## RestRequestFindTrades Objects

```python
class RestRequestFindTrades(RestRequestFindWithPagination)
```

**Attributes**:

- `market` - Base-quote pair e.g. 'IDEX-ETH'
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Trades created at the same timestamp or after from_id

<a id="idex_types.rest.request.RestRequestFindWithdrawal"></a>

## RestRequestFindWithdrawal Objects

```python
class RestRequestFindWithdrawal(RestRequestFindByWallet)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
  withdrawalId

<a id="idex_types.rest.request.RestRequestFindWithdrawals"></a>

## RestRequestFindWithdrawals Objects

```python
class RestRequestFindWithdrawals(RestRequestFindByWallet,
                                 RestRequestFindWithPagination)
```

**Attributes**:

- `nonce` - UUIDv1
  wallet
- `asset` - Asset by symbol
- `assetContractAddress` - Asset by contract address
- `start` - Starting timestamp (inclusive)
- `end` - Ending timestamp (inclusive)
- `limit` - Max results to return from 1-1000
- `fromId` - Withdrawals created after the fromId

<a id="idex_types.rest.request.RestRequestAssociateWallet"></a>

## RestRequestAssociateWallet Objects

```python
class RestRequestAssociateWallet(TypedDict)
```

**Attributes**:

- `nonce` - UUIDv1
- `wallet` - The wallet to associate with the authenticated account

<a id="idex_types.rest"></a>

# idex\_types.rest

<a id="idex_types.rest.response"></a>

# idex\_types.rest.response

<a id="idex_types.rest.response.RestResponseBalance"></a>

## RestResponseBalance Objects

```python
class RestResponseBalance(TypedDict)
```

**Attributes**:

- `asset` - Asset symbol
- `quantity` - Total quantity of the asset held by the wallet on the exchange
- `availableForTrade` - Quantity of the asset available for trading; quantity: locked
- `locked` - Quantity of the asset held in trades on the order book
- `usdValue` - Total value of the asset held by the wallet on the exchange in USD

<a id="idex_types.rest.response.RestResponseCandle"></a>

## RestResponseCandle Objects

```python
class RestResponseCandle(TypedDict)
```

**Attributes**:

- `start` - Time of the start of the interval
- `open` - Price of the first fill of the interval in quote terms
- `high` - Price of the highest fill of the interval in quote terms
- `low` - Price of the lowest fill of the interval in quote terms
- `close` - Price of the last fill of the interval in quote terms
- `volume` - Total volume of the period in base terms
- `sequence` - Fill sequence number of the last trade in the interval

<a id="idex_types.rest.response.RestResponseDeposit"></a>

## RestResponseDeposit Objects

```python
class RestResponseDeposit(TypedDict)
```

Asset deposits into smart contract

**Attributes**:

- `depositId` - IDEX-issued deposit identifier
- `asset` - Asset by symbol
- `quantity` - Deposit amount in asset terms
- `txId` - Ethereum transaction hash
- `txTime` - Timestamp of the Ethereum deposit transaction
- `confirmationTime` - Timestamp of credit on IDEX including block confirmations

<a id="idex_types.rest.response.RestResponseExchangeInfo"></a>

## RestResponseExchangeInfo Objects

```python
class RestResponseExchangeInfo(TypedDict)
```

**Attributes**:

- `timeZone` - Server time zone, always UTC
- `serverTime` - Current server time
- `maticDepositContractAddress` - Polygon address of the exchange smart contract for deposits
- `maticCustodyContractAddress` - Polygon address of the custody smart contract for certain add
  and remove liquidity calls
- `maticUsdPrice` - Current price of MATIC in USD
- `gasPrice` - Current gas price used by the exchange for trade settlement and withdrawal
  transactions in Gwei
- `volume24hUsd` - Total exchange trading volume for the trailing 24 hours in USD
- `totalVolumeUsd` - Total exchange trading volume for IDEX v3 on Polygon in USD
- `totalTrades` - Total number of trade executions for IDEX v3 on Polygon
- `totalValueLockedUsd` - Total value locked in IDEX v3 on Polygon in USD
- `idexTokenAddress` - Token contract address for the IDEX token on Polygon
- `idexUsdPrice` - Current price of the IDEX token in USD
- `idexMarketCapUsd` - Market capitalization of the IDEX token in USD
- `makerFeeRate` - Maker trade fee rate
- `takerFeeRate` - Total taker trade fee rate
- `takerIdexFeeRate` - Taker trade fee rate collected by IDEX; used in computing synthetic
  price levels for real-time order books
- `takerLiquidityProviderFeeRate` - Taker trade fee rate collected by liquidity providers; used
  in computing synthetic price levels for real-time order books
- `makerTradeMinimum` - Minimum size of an order that can rest on the order book in MATIC,
  applies to both MATIC and tokens
- `takerTradeMinimum` - Minimum order size that is accepted by the matching engine for
  execution in MATIC, applies to both MATIC and tokens
- `withdrawMinimum` - Minimum withdrawal amount in MATIC, applies to both MATIC and tokens
- `liquidityAdditionMinimum` - Minimum liquidity addition amount in MATIC, applies to both
  MATIC and tokens
- `liquidityRemovalMinimum` - Minimum withdrawal amount in MATIC, applies to both
  MATIC and tokens
- `blockConfirmationDelay` - Minimum number of block confirmations before on-chain transactions
  are processed

<a id="idex_types.rest.response.RestResponseOrderFill"></a>

## RestResponseOrderFill Objects

```python
class RestResponseOrderFill(_RestResponseOrderFillRequiredAttribs)
```

**Attributes**:

- `fillId` - Internal ID of fill
- `price` - Executed price of fill in quote terms
- `quantity` - Executed quantity of fill in base terms
- `quoteQuantity` - Executed quantity of trade in quote terms
- `orderBookQuantity` - Quantity of the fill in base terms supplied by order book liquidity,
  omitted for pool fills
- `orderBookQuoteQuantity` - Quantity of the fill in quote terms supplied by order book
  liquidity, omitted for pool fills
- `poolQuantity` - Quantity of the fill in base terms supplied by pool liquidity, omitted for
  orderBook fills
- `poolQuoteQuantity` - Quantity of the fill in quote terms supplied by pool liquidity, omitted
  for orderBook fills
- `time` - Fill timestamp
- `makerSide` - Which side of the order the liquidity maker was on
- `sequence` - Last trade sequence number for the market
- `fee` - Fee amount on fill
- `feeAsset` - Which token the fee was taken in
  gas
  liquidity
- `type` - orderBook, pool, or hybrid
- `txId` - Ethereum transaction ID, if available
- `txStatus` - Ethereum transaction status

<a id="idex_types.rest.response.RestResponseFill"></a>

## RestResponseFill Objects

```python
class RestResponseFill(_RestResponseFillRequiredAttribs)
```

**Attributes**:

- `fillId` - Internal ID of fill
- `price` - Executed price of fill in quote terms
- `quantity` - Executed quantity of fill in base terms
- `quoteQuantity` - Executed quantity of fill in quote terms
- `orderBookQuantity` - Quantity of the fill in base terms supplied by order book liquidity,
  omitted for pool fills
- `orderBookQuoteQuantity` - Quantity of the fill in quote terms supplied by order book
  liquidity, omitted for pool fills
- `poolQuantity` - Quantity of the fill in base terms supplied by pool liquidity, omitted for
  orderBook fills
- `poolQuoteQuantity` - Quantity of the fill in quote terms supplied by pool liquidity, omitted
  for orderBook fills
- `time` - Fill timestamp
- `makerSide` - Which side of the order the liquidity maker was on
- `sequence` - Last trade sequence number for the market
- `market` - Base-quote pair e.g. 'IDEX-ETH'
- `orderId` - Internal ID of order
- `clientOrderId` - Client-provided ID of order
- `side` - Orders side, buy or sell
- `fee` - Fee amount on fill
- `feeAsset` - Which token the fee was taken in
- `gas` - Amount collected to cover trade settlement gas costs, only present for taker
- `liquidity` - Whether the fill is the maker or taker in the trade from the perspective of the
  requesting API account, maker or taker
- `type` - Fill type
- `txId` - Ethereum transaction ID, if available
- `txStatus` - Ethereum transaction status

<a id="idex_types.rest.response.RestResponseLiquidityPool"></a>

## RestResponseLiquidityPool Objects

```python
class RestResponseLiquidityPool(TypedDict)
```

**Attributes**:

- `tokenA` - Address of one reserve token
- `tokenB` - Address of one reserve token
- `reserveA` - Quantity of token A held as reserve in token precision, not pips
- `reserveB` - Quantity of token B held as reserve in token precision, not pips
- `liquidityToken` - Address of the liquidity provider (LP) token
- `totalLiquidity` - Total quantity of liquidity provider (LP) tokens minted in token
  precision, not pips
- `reserveUsd` - Total value of reserves in USD
- `market` - Market symbol of pool's associated hybrid market

<a id="idex_types.rest.response.RestResponseLiquidityAddition"></a>

## RestResponseLiquidityAddition Objects

```python
class RestResponseLiquidityAddition(RestResponseLiquidityBase)
```

**Attributes**:

- `liquidityAdditionId` - Internal ID of liquidity addition
- `tokenA` - Asset symbol
- `tokenB` - Asset symbol
- `amountA` - Amount of tokenA added to the liquidity pool
- `amountB` - Amount of tokenB added to the liquidity pool
- `liquidity` - Amount of liquidity provided (LP) tokens minted
- `time` - Liquidity addition timestamp
- `initiatingTxId` - On chain initiated transaction ID, if available
- `errorCode` - Error short code present on liquidity addition error
- `errorMessage` - Human-readable error message present on liquidity addition error
- `feeTokenA` - Amount of tokenA collected as fees
- `feeTokenB` - Amount of tokenB collected as fees
- `txId` - Ethereum transaction ID, if available
- `txStatus` - Ethereum transaction status

<a id="idex_types.rest.response.RestResponseLiquidityPoolReserves"></a>

## RestResponseLiquidityPoolReserves Objects

```python
class RestResponseLiquidityPoolReserves(TypedDict)
```

**Attributes**:

- `baseReserveQuantity` - reserve quantity of base asset in pool
- `quoteReserveQuantity` - reserve quantity of quote asset in pool

<a id="idex_types.rest.response.RestResponseLiquidityRemoval"></a>

## RestResponseLiquidityRemoval Objects

```python
class RestResponseLiquidityRemoval(RestResponseLiquidityBase)
```

**Attributes**:

- `liquidityRemovalId` - Internal ID of liquidity removal
- `tokenA` - Asset symbol
- `tokenB` - Asset symbol
- `amountA` - Amount of tokenA added to the liquidity pool
- `amountB` - Amount of tokenB added to the liquidity pool
- `liquidity` - Amount of liquidity provided (LP) tokens minted
- `time` - Liquidity addition timestamp
- `initiatingTxId` - On chain initiated transaction ID, if available
- `errorCode` - Error short code present on liquidity addition error
- `errorMessage` - Human-readable error message present on liquidity addition error
- `feeTokenA` - Amount of tokenA collected as fees
- `feeTokenB` - Amount of tokenB collected as fees
- `txId` - Ethereum transaction ID, if available
- `txStatus` - Ethereum transaction status

<a id="idex_types.rest.response.RestResponseMarket"></a>

## RestResponseMarket Objects

```python
class RestResponseMarket(TypedDict)
```

**Attributes**:

- `market` - Market symbol
- `type` - Market type
- `status` - Market trading status
- `baseAsset` - Base asset symbol
- `baseAssetPrecision` - Exchange decimal precision of the base asset, always 8 due to
  precision normalization
- `quoteAsset` - Quote asset symbol
- `quoteAssetPrecision` - Exchange decimal precision of the base asset, always 8 due to
  precision normalization
- `makerFeeRate` - Maker trade fee rate
- `takerFeeRate` - Total taker trade fee rate
- `takerIdexFeeRate` - Taker trade fee rate collected by IDEX; used in computing synthetic
  price levels for real-time order books
- `takerLiquidityProviderFeeRate` - Taker trade fee rate collected by liquidity providers; used
  in computing synthetic price levels for real-time order books
- `tickSize` - Market tick size (minimum change in order price)

<a id="idex_types.rest.response.RestResponseOrder"></a>

## RestResponseOrder Objects

```python
class RestResponseOrder(_RestResponseOrderRequiredAttribs)
```

**Attributes**:

- `market` - Market symbol as base-quote pair e.g. 'IDEX-ETH'
- `orderId` - Exchange-assigned order identifier
- `clientOrderId` - Client-specified order identifier
- `wallet` - Ethereum address of placing wallet
- `time` - Time of initial order processing by the matching engine
- `status` - Current order status
- `errorCode` - Error short code explaining order error or failed batch cancel
- `errorMessage` - Error description explaining order error or failed batch cancel
- `type` - Order type
- `side` - Order side
- `originalQuantity` - Original quantity specified by the order in base terms, omitted for
  market orders specified in quote terms
- `originalQuoteQuantity` - Original quantity specified by the order in quote terms, only
  present for market orders specified in quote terms
- `executedQuantity` - Quantity that has been executed in base terms
- `cumulativeQuoteQuantity` - Cumulative quantity that has been spent (buy orders) or received
  (sell orders) in quote terms, omitted if unavailable for historical orders
- `avgExecutionPrice` - Weighted average price of fills associated with the order; only present
  with fills
  price -	Original price specified by the order in quote terms, omitted for all market orders
- `stopPrice` - Stop loss or take profit price, only present for stopLoss, stopLossLimit,
  takeProfit, and takeProfitLimit orders
- `timeInForce` - Time in force policy, see values, only present for limit orders
- `selfTradePrevention` - Self-trade prevention policy, see values
- `fills` - Array of order fill objects

<a id="idex_types.rest.response.RestResponseTicker"></a>

## RestResponseTicker Objects

```python
class RestResponseTicker(TypedDict)
```

**Attributes**:

- `market` - Base-quote pair e.g. 'IDEX-ETH'
- `time` - Time when data was calculated, open and change is assumed to be trailing 24h
- `open` - Price of the first trade for the period in quote terms
- `high` - Highest traded price in the period in quote terms
- `low` - Lowest traded price in the period in quote terms
- `close` - Same as last
- `closeQuantity` - Quantity of the last period in base terms
- `baseVolume` - 24h volume in base terms
- `quoteVolume` - 24h volume in quote terms
- `percentChange` - % change from open to close
- `numTrades` - Number of fills for the market in the period
- `ask` - Best ask price on the order book
- `bid` - Best bid price on the order book
- `sequence` - Last trade sequence number for the market

<a id="idex_types.rest.response.RestResponseTrade"></a>

## RestResponseTrade Objects

```python
class RestResponseTrade(TypedDict)
```

**Attributes**:

- `fillId` - Internal ID of fill
- `price` - Executed price of trade in quote terms
- `quantity` - Executed quantity of trade in base terms
- `quoteQuantity` - Executed quantity of trade in quote terms
- `time` - Fill timestamp
- `makerSide` - Which side of the order the liquidity maker was on
- `type` - orderBook, pool, or hybrid
- `sequence` - Last trade sequence number for the market

<a id="idex_types.rest.response.RestResponseUser"></a>

## RestResponseUser Objects

```python
class RestResponseUser(TypedDict)
```

**Attributes**:

- `depositEnabled` - Deposits are enabled for the user account
- `orderEnabled` - Placing orders is enabled for the user account
- `cancelEnabled` - Cancelling orders is enabled for the user account
- `withdrawEnabled` - Withdrawals are enabled for the user account
- `totalPortfolioValueUsd` - Total value of all holdings deposited on the exchange,
  for all wallets associated with the user account, in USD
- `makerFeeRate` - User-specific maker trade fee rate
- `takerFeeRate` - User-specific taker trade fee rate
- `takerIdexFeeRate` - User-specific liquidity pool taker IDEX fee rate
- `takerLiquidityProviderFeeRate` - User-specific liquidity pool taker LP provider fee rate

<a id="idex_types.rest.response.RestResponseWallet"></a>

## RestResponseWallet Objects

```python
class RestResponseWallet(TypedDict)
```

**Attributes**:

- `address` - Ethereum address of the wallet
- `totalPortfolioValueUsd` - Total value of all holdings deposited on the exchange for the
  wallet in USD
- `time` - Timestamp of association of the wallet with the user account

<a id="idex_types.rest.response.RestResponseWithdrawal"></a>

## RestResponseWithdrawal Objects

```python
class RestResponseWithdrawal(RestResponseWithdrawalBase)
```

**Attributes**:

- `withdrawalId` - Exchange-assigned withdrawal identifier
- `asset` - Symbol of the withdrawn asset, exclusive with assetContractAddress
- `assetContractAddress]` - Token contract address of withdrawn asset, exclusive with asset
- `quantity` - Quantity of the withdrawal
- `time` - Timestamp of withdrawal API request
- `fee` - Amount deducted from withdrawal to cover IDEX-paid gas
- `txId` - Ethereum transaction ID, if available
- `txStatus` - Ethereum transaction status

<a id="idex_types.rest.response.RestResponseAssociateWallet"></a>

## RestResponseAssociateWallet Objects

```python
class RestResponseAssociateWallet(TypedDict)
```

**Attributes**:

- `address` - Ethereum address of the wallet
- `totalPortfolioValueUsd` - Total value of all holdings deposited on the exchange for the
  wallet in USD
- `time` - Timestamp of association of the wallet with the user account

<a id="order_book"></a>

# order\_book

<a id="order_book.api_conversions"></a>

# order\_book.api\_conversions

<a id="order_book.hybrid"></a>

# order\_book.hybrid

<a id="order_book.hybrid.l2_limit_order_book_to_hybrid_order_books"></a>

#### l2\_limit\_order\_book\_to\_hybrid\_order\_books

```python
def l2_limit_order_book_to_hybrid_order_books(
        order_book: L2OrderBook,
        idex_fee_rate: int,
        pool_fee_rate: int,
        include_minimum_taker_levels: bool,
        minimum_taker_in_quote: Optional[int],
        tick_size: int,
        visible_levels: int = 10,
        visible_slippage: int = 100) -> L1AndL2OrderBook
```

Convert a limit-order orderbook and a liquidity pool to a hybrid order book representation

**Arguments**:

- `order_book` - L2 book, e.g. from GET /v1/orderbook?level=2&limitOrderOnly=true
- `visible_levels` - number of price levels to calculate, default = 10 asks, 10 bids
- `visible_slippage` - price slippage per level, in increments of 0.001%, default = 100 (0.1%)
- `idex_fee_rate` - trade fee rate charged by IDEX, expressed in pips
- `pool_fee_rate` - pool fee rate chared by liquidity pool, expressed in pips
- `include_minimum_taker_levels` - if true, calculate a synthetic price level at twice
  the minimum trade size
- `minimum_taker_in_quote` - minimum trade size expressed in pips, or null if none available
- `tick_size` - minimum price movement expressed in pips (10^-8)

<a id="order_book.quantities"></a>

# order\_book.quantities

<a id="order_book.quantities.calculate_gross_base_quantity"></a>

#### calculate\_gross\_base\_quantity

```python
def calculate_gross_base_quantity(base_asset_quantity: int,
                                  quote_asset_quantity: int, target_price: int,
                                  idex_fee_rate: int,
                                  pool_fee_rate: int) -> int
```

Helper function to calculate gross base quantity available at a bid price.
See quantities_available_from_pool_at_bid_price.

<a id="order_book.quantities.calculate_gross_base_value_of_buy_quantities"></a>

#### calculate\_gross\_base\_value\_of\_buy\_quantities

```python
def calculate_gross_base_value_of_buy_quantities(
        base_asset_quantity: int, quote_asset_quantity: int,
        gross_quote_quantity: int) -> int
```

Helper function to convert from quote to base quantities.
See quantities_available_from_pool_at_ask_price.

<a id="order_book.quantities.calculate_gross_quote_quantity"></a>

#### calculate\_gross\_quote\_quantity

```python
def calculate_gross_quote_quantity(base_asset_quantity: int,
                                   quote_asset_quantity: int,
                                   target_price: int, idex_fee_rate: int,
                                   pool_fee_rate: int) -> int
```

Helper function to calculate gross quote available at a bid price.
See quantities_available_from_pool_at_bid_price.

<a id="order_book.quantities.calculate_gross_quote_value_of_sell_quantities"></a>

#### calculate\_gross\_quote\_value\_of\_sell\_quantities

```python
def calculate_gross_quote_value_of_sell_quantities(
        base_asset_quantity: int, quote_asset_quantity: int,
        gross_base_quantity: int) -> int
```

Helper function to convert from base to quote quantities.
See quantities_available_from_pool_at_bid_price.

<a id="order_book.quantities.calculate_base_quantity_out"></a>

#### calculate\_base\_quantity\_out

```python
def calculate_base_quantity_out(base_asset_quantity: int,
                                quote_asset_quantity: int,
                                gross_quote_quantity_in: int,
                                idex_fee_rate: int, pool_fee_rate: int) -> int
```

Given a taker order size expressed in quote, how much base is received from the pool.
See l1or_l2_best_available_prices.

<a id="order_book.quantities.calculate_quote_quantity_out"></a>

#### calculate\_quote\_quantity\_out

```python
def calculate_quote_quantity_out(base_asset_quantity: int,
                                 quote_asset_quantity: int,
                                 gross_base_quantity_in: int,
                                 idex_fee_rate: int,
                                 pool_fee_rate: int) -> int
```

Given a taker order size expressed in base, how much quote is received from the pool.
See l1_or_l2_best_available_prices.

<a id="order_book.quantities.calculate_synthetic_price_levels"></a>

#### calculate\_synthetic\_price\_levels

```python
def calculate_synthetic_price_levels(
        base_asset_quantity: int,
        quote_asset_quantity: int,
        visible_levels: int,
        visible_slippage: int,
        idex_fee_rate: int = 0,
        pool_fee_rate: int = 0,
        tick_size: int = 1) -> SyntheticL2OrderBook
```

Generates a synthetic orderbook consisting of price levels for pool liquidity only

**Arguments**:

- `base_asset_quantity` - pool reserve in base asset, must be at least 1.0 expressed
  in pips (10^-8)
- `quote_asset_quantity` - pool reserve in quote asset, must be at least 1.0 expressed
  in pips (10^-8)
- `visible_levels` - how many ask and bid price levels to generate (of each)
- `visible_slippage` - how much slippage per price level, in 1/1000th of a percent (100 = 0.1%)
- `idex_fee_rate` - the idex fee rate to use for calculations (query /v1/exchange for current
  global setting)
- `pool_fee_rate` - the liquidity pool fee rate to use for calculations (query /v1/exchange for
  current global setting)
- `tick_size` - minimum price movement expressed in pips (10^-8)
  

**Returns**:

  A level 2 order book with synthetic price levels only

<a id="order_book.quantities.recalculate_hybrid_level_amounts"></a>

#### recalculate\_hybrid\_level\_amounts

```python
def recalculate_hybrid_level_amounts(orderbook: L2OrderBook,
                                     idex_fee_rate: int,
                                     pool_fee_rate: int) -> L2OrderBook
```

Recalculate price level quantities for a book previously sorted with
sort_and_merge_levels_unadjusted

**Arguments**:

- `orderbook` - an unadjusted level 2 order book as returned by {sortAndMergeLevelsUnadjusted}
- `idex_fee_rate` - idex fee rate to use in pool quantity calculations
- `pool_fee_rate` - pool fee rate to use in pool quantity calculations

<a id="order_book.quantities.sort_and_merge_levels_unadjusted"></a>

#### sort\_and\_merge\_levels\_unadjusted

```python
def sort_and_merge_levels_unadjusted(
    limit_order_levels: List[OrderBookLevelL2],
    synthetic_levels: List[OrderBookLevelL2],
    is_before: Callable[[OrderBookLevelL2, OrderBookLevelL2], bool]
) -> List[OrderBookLevelL2]
```

Combines limit orders and synthetic price levels into an intermediate sorted state
IMPORTANT: this function does not update price level quantities after merging

**Arguments**:

- `limit_order_levels` - a level 2 orderbook with only limit orders
- `synthetic_levels` - a level 2 orderbook with only synthetic orders
- `is_before` - comparison function for sorting price levels
  

**Returns**:

  Level 2 order book with synthetic price levels only

<a id="order_book.quantities.quantities_available_from_pool_at_ask_price"></a>

#### quantities\_available\_from\_pool\_at\_ask\_price

```python
def quantities_available_from_pool_at_ask_price(
        base_asset_quantity: int, quote_asset_quantity: int, ask_price: int,
        idex_fee_rate: int, pool_fee_rate: int) -> PriceLevelQuantities
```

Helper function to calculate the asset quantities available at a given price level
(pool liquidity only)

**Arguments**:

- `base_asset_quantity` - pool reserve in base asset, must be at least 1.0 expressed
  in pips (10^-8)
- `quote_asset_quantity` - pool reserve in quote asset, must be at least 1.0 expressed
  in pips (10^-8)
- `ask_price` - the ask price level to calculate quantities for
- `idex_fee_rate` - the idex fee rate to use for calculations (query /v1/exchange for
  current global setting)
- `pool_fee_rate` - the liquidity pool fee rate to use for calculations (query /v1/exchange for
  current global setting)
  

**Returns**:

  Level 2 order book with synthetic price levels only

<a id="order_book.quantities.quantities_available_from_pool_at_bid_price"></a>

#### quantities\_available\_from\_pool\_at\_bid\_price

```python
def quantities_available_from_pool_at_bid_price(
        base_asset_quantity: int, quote_asset_quantity: int, bid_price: int,
        idex_fee_rate: int, pool_fee_rate: int) -> PriceLevelQuantities
```

Helper function to calculate the asset quantities available at a given price level
(pool liquidity only)

**Arguments**:

- `base_asset_quantity` - pool reserve in base asset, must be at least 1.0
  expressed in pips (10^-8)
- `quote_asset_quantity` - pool reserve in quote asset, must be at least 1.0
  expressed in pips (10^-8)
- `bid_price` - the bid price level to calculate quantities for
- `idex_fee_rate` - the idex fee rate to use for calculations (query /v1/exchange for
  current global setting)
- `pool_fee_rate` - the liquidity pool fee rate to use for calculations (query /v1/exchange for
  current global setting)
  

**Returns**:

  Level 2 order book with synthetic price levels only

<a id="order_book.quantities.aggregate_l2_order_book_at_tick_size"></a>

#### aggregate\_l2\_order\_book\_at\_tick\_size

```python
def aggregate_l2_order_book_at_tick_size(input_book: L2OrderBook,
                                         tick_size: int) -> L2OrderBook
```

Helper function to re-aggregate L2 orderbook price levels at a larger (more zeroes) tick size

<a id="order_book.quantities.l1_or_l2_best_available_prices"></a>

#### l1\_or\_l2\_best\_available\_prices

```python
def l1_or_l2_best_available_prices(pool: PoolReserveQuantities,
                                   idex_fee_rate: int, pool_fee_rate: int,
                                   taker_minimum_in_base: int,
                                   taker_minimum_in_quote: int,
                                   tick_size: int) -> BestAvailablePriceLevels
```

Given a minimum taker order size, calculate the best achievable price level using
pool liquidity only.

**Arguments**:

- `pool` - pool reserve quantities for the orderbook in question
- `idex_fee_rate` - the idex fee rate to use for pool calculations
- `pool_fee_rate` - the pool fee rate to use for pool calculations
- `taker_minimum_in_base` - the minimum taker order size, expressed in base asset units
- `taker_minimum_in_quote` - the minimum taker order size, expressed in quote asset units

<a id="order_book.quantities.l1_l2_order_books_with_minimum_taker"></a>

#### l1\_l2\_order\_books\_with\_minimum\_taker

```python
def l1_l2_order_books_with_minimum_taker(l2: L2OrderBook, idex_fee_rate: int,
                                         pool_fee_rate: int,
                                         taker_minimum_in_quote: int,
                                         tick_size: int) -> L1AndL2OrderBook
```

Modifies an existing level 2 order book to include better price levels at the desired taker
order size, if available from pool reserves.

**Arguments**:

- `pool` - pool reserve quantities for the orderbook in question
- `idexFeeRate` - the idex fee rate to use for pool calculations
- `poolFeeRate` - the pool fee rate to use for pool calculations
- `takerMinimumInQuote` - the minimum taker order size, expressed in quote asset units
  

**Returns**:

  The resulting level 1 and level 2 orderbooks

<a id="order_book.quantities.validate_synthetic_price_level_inputs"></a>

#### validate\_synthetic\_price\_level\_inputs

```python
def validate_synthetic_price_level_inputs(base_asset_quantity: int,
                                          quote_asset_quantity: int,
                                          target_price: int,
                                          is_buy: bool) -> None
```

Validates assumptions for reserve quantities and pricing required for quantity calculations

**Arguments**:

- `base_asset_quantity` - pool reserve in base asset, must be at least 1.0 expressed
  in pips (10^-8)
- `quote_asset_quantity` - pool reserve in quote asset, must be at least 1.0 expressed
  in pips (10^-8)
- `target_price` - price expressed in pips, must be 0 < price < 2^64-1 and on the correct side
  of the spread
- `is_buy` - if true, the price is targeting buy orders (bids), otherwise sell orders (asks)
  

**Returns**:

  None, validation always succeeds or raises an exception

<a id="order_book.quantities.adjust_price_to_tick_size"></a>

#### adjust\_price\_to\_tick\_size

```python
def adjust_price_to_tick_size(
        price: int,
        tick_size: int,
        rounding_mode: RoundingMode = DEFAULT_ROUNDING_MODE) -> int
```

Adjusts prices in pips to account for tick size by discarding insignificant digits using
specified rounding mode. Ex price 123456789 at tick size 1 is 123456789, at tick size 10
123456780, at 100 123456700, etc

<a id="order_book.utils"></a>

# order\_book.utils

<a id="order_book.utils.l2_to_l1_order_book"></a>

#### l2\_to\_l1\_order\_book

```python
def l2_to_l1_order_book(l2: L2OrderBook) -> L1OrderBook
```

Derive the level 1 orderbook from a level 2 orderbook

<a id="client"></a>

# client

<a id="client.websocket.client"></a>

# client.websocket.client

<a id="client.websocket.client.WebSocketClient"></a>

## WebSocketClient Objects

```python
class WebSocketClient()
```

WebSocket API client

When apiKey and apiSecret are provided, the client will automatically handle
WebSocket authentication token generation and refresh. Omit when using only public
WebSocket subscriptions.

<a id="client.websocket.client.WebSocketClient.__init__"></a>

#### \_\_init\_\_

```python
def __init__(api_key: Optional[str] = None,
             api_secret: Optional[str] = None,
             should_reconnect_automatically: bool = False,
             connect_timeout: Optional[int] = None,
             sandbox: bool = False,
             multiverse_chain: MultiverseChain = MultiverseChain.MATIC,
             base_url: Optional[str] = None,
             websocket_auth_token_fetch: Optional[Callable[[str],
                                                           str]] = None)
```

**Arguments**:

- `api_key` - Used to authenticate user when automatically refreshing WS token
- `api_secret` - Used to compute HMAC signature when automatically refreshing WS token
  receiving push updates. Eg. {market}@{subscription}_{option}
- `should_reconnect_automatically` - If true, automatically reconnects when connection is
  closed by the server or network errors
- `connect_timeout` - Timeout (in milliseconds) before failing when trying to connect to
  the WebSocket. Defaults to 5000.
- `sandbox` - If true, client will point to API sandbox
- `multiverse_chain` - Which multiverse chain the client will point to

<a id="client.websocket.client.WebSocketClient.connect"></a>

#### connect

```python
async def connect() -> None
```

Establish a WebSocket connection to the API and start listening for messages

<a id="client.websocket.client.WebSocketClient.subscribe_authenticated"></a>

#### subscribe\_authenticated

```python
async def subscribe_authenticated(subscriptions: Sequence[
    AuthTokenWebSocketRequestAuthenticatedSubscription],
                                  markets: List[str] = None,
                                  cid: str = None) -> None
```

Strictly typed subscribe which only can be used on authenticated subscriptions.

See https://api-docs-v3.idex.io/`websocket`-subscriptions

**Arguments**:

  subscriptions
- `markets` - Optionally provide top level markets
- `cid` - Optional custom identifier to identify the matching response

<a id="client.websocket.client.WebSocketClient.subscribe_unauthenticated"></a>

#### subscribe\_unauthenticated

```python
async def subscribe_unauthenticated(
        subscriptions: Sequence[WebSocketRequestUnauthenticatedSubscription],
        markets: List[str] = None,
        cid: str = None) -> None
```

Strictly typed subscribe which only can be used on non-authenticated subscriptions.

See https://api-docs-v3.idex.io/`websocket`-subscriptions

**Arguments**:

  subscriptions
- `markets` - Optionally provide top level markets
- `cid` - Optional custom identifier to identify the matching response

<a id="client.websocket.client.WebSocketClient.subscribe"></a>

#### subscribe

```python
async def subscribe(subscriptions: Sequence[
    Union[WebSocketRequestSubscription,
          WebSocketRequestUnauthenticatedSubscriptionNameOnly, ]],
                    markets: List[str] = None,
                    cid: str = None) -> None
```

Subscribe to a given set of subscriptions, optionally providing a list of top level markets
or a cid property.

See https://api-docs-v3.idex.io/`websocket`-subscriptions

**Arguments**:

  subscriptions
- `markets` - Optionally provide top level markets
- `cid` - Optional custom identifier to identify the matching response

<a id="client.websocket.client.WebSocketClient.reconnect"></a>

#### reconnect

```python
async def reconnect() -> None
```

Reconnect with exponential backoff

<a id="client.websocket"></a>

# client.websocket

<a id="client.websocket.utils"></a>

# client.websocket.utils

<a id="client.websocket.transform"></a>

# client.websocket.transform

<a id="client.utils"></a>

# client.utils

<a id="client.order_book"></a>

# client.order\_book

<a id="client.order_book.real_time"></a>

# client.order\_book.real\_time

<a id="client.order_book.real_time.OrderBookRealTimeClient"></a>

## OrderBookRealTimeClient Objects

```python
class OrderBookRealTimeClient(AsyncIOEventEmitter)
```

<a id="client.order_book.real_time.OrderBookRealTimeClient.start"></a>

#### start

```python
async def start(markets: List[str]) -> None
```

Loads initial state from REST API and begin listening to orderbook updates.

<a id="client.order_book.real_time.OrderBookRealTimeClient.stop"></a>

#### stop

```python
async def stop() -> None
```

Stop the order book client, and reset internal state. Call this when you are no longer
using the client, to release memory and network resources.

<a id="client.order_book.real_time.OrderBookRealTimeClient.set_fees_and_minimums_override"></a>

#### set\_fees\_and\_minimums\_override

```python
def set_fees_and_minimums_override(override: OrderBookFeesAndMinimums) -> None
```

Set custom fee rates for synthetic price level calculations. Use this if your wallet has
custom fees set.

<a id="client.order_book.real_time.OrderBookRealTimeClient.get_order_book_l1"></a>

#### get\_order\_book\_l1

```python
def get_order_book_l1(market: str,
                      tick_size: Optional[int] = None
                      ) -> RestResponseOrderBook
```

Load the current state of the level 1 orderbook for this market.

**Arguments**:

  market
- `tick_size` - minimum price movement expressed in pips (10^-8), defaults to market setting

<a id="client.order_book.real_time.OrderBookRealTimeClient.get_order_book_l2"></a>

#### get\_order\_book\_l2

```python
def get_order_book_l2(
        market: str,
        limit: int = 100,
        tick_size: Optional[int] = None) -> RestResponseOrderBook
```

Load the current state of the level 2 orderbook for this market.

**Arguments**:

  market
- `limit` - Total number of price levels (bids + asks) to return, between 2 and 1000
- `tickSize` - minimum price movement expressed in pips (10^-8)

<a id="client.order_book.utils"></a>

# client.order\_book.utils

<a id="client.order_book.utils.l1_equal"></a>

#### l1\_equal

```python
def l1_equal(before_l1: L1OrderBook, after_l1: L1OrderBook) -> bool
```

Determine whether two level 1 order books are equal, including pool reserves

<a id="client.order_book.utils.update_l2_side"></a>

#### update\_l2\_side

```python
def update_l2_side(is_ascending: bool, side: List[OrderBookLevelL2],
                   updates: List[OrderBookLevelL2]) -> List[OrderBookLevelL2]
```

Applies a changeset to a single side of the orderbook

Params:
is_ascending: true for asks, false for bids (ordering of price levels)
side
updates

**Returns**:

  Updated order book side

<a id="client.order_book.utils.update_l2_levels"></a>

#### update\_l2\_levels

```python
def update_l2_levels(book: L2OrderBook, updated_levels: L2OrderBook) -> None
```

Updates a level 2 orderbook using a partial "diff" received over websockets

**Arguments**:

- `book` - level 2 orderbook to update
- `updated_levels` - level 2 orderbook containing only limit order price levels that
  have changed

<a id="client.rest.public"></a>

# client.rest.public

<a id="client.rest.public.RestPublicClient"></a>

## RestPublicClient Objects

```python
class RestPublicClient()
```

<a id="client.rest.public.RestPublicClient.ping"></a>

#### ping

```python
def ping() -> Dict
```

Test connectivity to the REST API
See https://api-docs-v3.idex.io/`get`-ping

<a id="client.rest.public.RestPublicClient.get_server_time"></a>

#### get\_server\_time

```python
def get_server_time() -> int
```

Returns the current server time
See https://api-docs-v3.idex.io/`get`-time

<a id="client.rest.public.RestPublicClient.get_exchange_info"></a>

#### get\_exchange\_info

```python
def get_exchange_info() -> RestResponseExchangeInfo
```

Returns basic information about the exchange
See https://api-docs-v3.idex.io/`get`-exchange

<a id="client.rest.public.RestPublicClient.get_assets"></a>

#### get\_assets

```python
def get_assets() -> List[RestResponseAsset]
```

Returns information about assets supported by the exchange
See https://api-docs-v3.idex.io/`get`-assets

<a id="client.rest.public.RestPublicClient.get_markets"></a>

#### get\_markets

```python
def get_markets(
    find_markets: Optional[RestRequestFindMarkets] = None
) -> List[RestResponseMarket]
```

Returns information about the currently listed markets
See https://api-docs-v3.idex.io/`get`-markets

<a id="client.rest.public.RestPublicClient.get_liquidity_pools"></a>

#### get\_liquidity\_pools

```python
def get_liquidity_pools(
    find_liquidity_pools: Optional[RestRequestFindLiquidityPools] = None
) -> List[RestResponseLiquidityPool]
```

Returns information about liquidity pools supported by the exchange
See https://api-docs-v3.idex.io/`get`-liquidity-pools

<a id="client.rest.public.RestPublicClient.get_tickers"></a>

#### get\_tickers

```python
def get_tickers(market: Optional[str] = None) -> List[RestResponseTicker]
```

Returns market statistics for the trailing 24-hour period

<a id="client.rest.public.RestPublicClient.get_candles"></a>

#### get\_candles

```python
def get_candles(
        find_candles: RestRequestFindCandles) -> List[RestResponseCandle]
```

Returns candle (OHLCV) data for a market
See https://api-docs-v3.idex.io/`get`-candles

<a id="client.rest.public.RestPublicClient.get_trades"></a>

#### get\_trades

```python
def get_trades(find_trades: RestRequestFindTrades) -> List[RestResponseTrade]
```

Returns public trade data for a market
See https://api-docs-v3.idex.io/`get`-trades

<a id="client.rest.public.RestPublicClient.get_order_book_level1"></a>

#### get\_order\_book\_level1

```python
def get_order_book_level1(
        market: str,
        limit_order_only: bool = False) -> List[RestResponseOrderBook]
```

Get current top bid/ask price levels of order book for a market
See https://api-docs-v3.idex.io/`get`-order-books

<a id="client.rest.public.RestPublicClient.get_order_book_level2"></a>

#### get\_order\_book\_level2

```python
def get_order_book_level2(
        market: str,
        limit: int = 50,
        limit_order_only: bool = False) -> RestResponseOrderBook
```

Get current order book price levels for a market
See https://api-docs-v3.idex.io/`get`-order-books

<a id="client.rest"></a>

# client.rest

<a id="client.rest.authenticated"></a>

# client.rest.authenticated

<a id="client.rest.authenticated.RestAuthenticatedClient"></a>

## RestAuthenticatedClient Objects

```python
class RestAuthenticatedClient()
```

<a id="client.rest.authenticated.RestAuthenticatedClient.add_liquidity"></a>

#### add\_liquidity

```python
def add_liquidity(
    req: request.RestRequestAddLiquidity,
    signer: Optional[sig.MessageSigner] = None,
    dependent_transactions: Optional[List[str]] = None
) -> response.RestResponseLiquidityAddition
```

Add liquidity to a hybrid liquidity pool from assets held by a wallet on the exchange

<a id="client.rest.authenticated.RestAuthenticatedClient.remove_liquidity"></a>

#### remove\_liquidity

```python
def remove_liquidity(
    req: request.RestRequestRemoveLiquidity,
    signer: Optional[sig.MessageSigner] = None,
    dependent_transactions: Optional[List[str]] = None
) -> response.RestResponseLiquidityRemoval
```

Remove liquidity from a hybrid liquidity pool represented by LP tokens held by a wallet
on the exchange

<a id="client.rest.authenticated.RestAuthenticatedClient.get_liquidity_addition"></a>

#### get\_liquidity\_addition

```python
def get_liquidity_addition(
    req: request.RestRequestFindLiquidityAddition
) -> Union[response.RestResponseLiquidityAddition,
           List[response.RestResponseLiquidityAddition]]
```

Returns information about a single liquidity addition from a wallet

<a id="client.rest.authenticated.RestAuthenticatedClient.get_liquidity_additions"></a>

#### get\_liquidity\_additions

```python
def get_liquidity_additions(
    req: request.RestRequestFindLiquidityChanges
) -> List[response.RestResponseLiquidityAddition]
```

Returns information about multiple liquidity additions from a wallet

<a id="client.rest.authenticated.RestAuthenticatedClient.get_liquidity_removal"></a>

#### get\_liquidity\_removal

```python
def get_liquidity_removal(
    req: request.RestRequestFindLiquidityRemoval
) -> response.RestResponseLiquidityRemoval
```

Returns information about a single liquidity removal from a wallet

<a id="client.rest.authenticated.RestAuthenticatedClient.get_liquidity_removals"></a>

#### get\_liquidity\_removals

```python
def get_liquidity_removals(
    req: request.RestRequestFindLiquidityChanges
) -> List[response.RestResponseLiquidityRemoval]
```

Returns information about multiple liquidity removals from a wallet

<a id="client.rest.authenticated.RestAuthenticatedClient.get_user"></a>

#### get\_user

```python
def get_user(nonce: str) -> response.RestResponseUser
```

Get account details for the API key's user
See https://api-docs-v3.idex.io/`get`-user-account

**Arguments**:

- `nonce` - UUIDv1
  

**Returns**:

  Information about the user

<a id="client.rest.authenticated.RestAuthenticatedClient.get_wallets"></a>

#### get\_wallets

```python
def get_wallets(nonce: str) -> List[response.RestResponseWallet]
```

Get account details for the API key's user
See https://api-docs-v3.idex.io/`get`-wallets

**Arguments**:

- `nonce` - UUIDv1
  

**Returns**:

  The user's wallets

<a id="client.rest.authenticated.RestAuthenticatedClient.get_balances"></a>

#### get\_balances

```python
def get_balances(
    req: request.RestRequestFindBalances
) -> List[response.RestResponseBalance]
```

Get asset quantity data (positions) held by a wallet on the exchange

<a id="client.rest.authenticated.RestAuthenticatedClient.associate_wallet"></a>

#### associate\_wallet

```python
def associate_wallet(
    req: request.RestRequestAssociateWallet,
    signer: Optional[sig.MessageSigner] = None
) -> response.RestResponseAssociateWallet
```

Associate a wallet with the authenticated account
See https://api-docs-v3.idex.io/`associate`-wallet

<a id="client.rest.authenticated.RestAuthenticatedClient.create_order"></a>

#### create\_order

```python
def create_order(
        req: request.RestRequestOrder,
        signer: Optional[sig.MessageSigner] = None
) -> response.RestResponseOrder
```

Create and submit an order to the matching engine
See https://api-docs-v3.idex.io/`create`-order

<a id="client.rest.authenticated.RestAuthenticatedClient.create_test_order"></a>

#### create\_test\_order

```python
def create_test_order(
        req: request.RestRequestOrder,
        signer: Optional[sig.MessageSigner] = None
) -> response.RestResponseOrder
```

Tests order creation and validation without submitting an order to the matching engine
See https://api-docs-v3.idex.io/`test`-create-order

<a id="client.rest.authenticated.RestAuthenticatedClient.cancel_order"></a>

#### cancel\_order

```python
def cancel_order(
    req: request.RestRequestCancelOrder,
    signer: Optional[sig.MessageSigner] = None
) -> List[response.RestResponseCanceledOrder]
```

Cancel a single order
See https://api-docs-v3.idex.io/`cancel`-order

<a id="client.rest.authenticated.RestAuthenticatedClient.cancel_orders"></a>

#### cancel\_orders

```python
def cancel_orders(
    req: request.RestRequestCancelOrder,
    signer: Optional[sig.MessageSigner] = None
) -> List[response.RestResponseCanceledOrder]
```

Cancel multiple orders
See https://api-docs-v3.idex.io/`cancel`-order

<a id="client.rest.authenticated.RestAuthenticatedClient.get_order"></a>

#### get\_order

```python
def get_order(req: request.RestRequestFindOrder) -> response.RestResponseOrder
```

Get an order
See https://api-docs-v3.idex.io/`get`-orders

<a id="client.rest.authenticated.RestAuthenticatedClient.get_orders"></a>

#### get\_orders

```python
def get_orders(
        req: request.RestRequestFindOrders
) -> List[response.RestResponseOrder]
```

Get multiple orders
See https://api-docs-v3.idex.io/`get`-orders

<a id="client.rest.authenticated.RestAuthenticatedClient.get_fill"></a>

#### get\_fill

```python
def get_fill(req: request.RestRequestFindFill) -> response.RestResponseFill
```

Get a fill
See https://api-docs-v3.idex.io/`get`-fills

<a id="client.rest.authenticated.RestAuthenticatedClient.get_fills"></a>

#### get\_fills

```python
def get_fills(
        req: request.RestRequestFindFills) -> List[response.RestResponseFill]
```

Get multiple fills
See https://api-docs-v3.idex.io/`get`-fills

<a id="client.rest.authenticated.RestAuthenticatedClient.get_deposit"></a>

#### get\_deposit

```python
def get_deposit(
        req: request.RestRequestFindDeposit) -> response.RestResponseDeposit
```

Get a fill
See https://api-docs-v3.idex.io/`get`-deposits

<a id="client.rest.authenticated.RestAuthenticatedClient.get_deposits"></a>

#### get\_deposits

```python
def get_deposits(
    req: request.RestRequestFindDeposits
) -> List[response.RestResponseDeposit]
```

Get a fill
See https://api-docs-v3.idex.io/`get`-deposits

<a id="client.rest.authenticated.RestAuthenticatedClient.withdraw"></a>

#### withdraw

```python
def withdraw(
    req: request.RestRequestWithdrawal,
    signer: Optional[sig.MessageSigner] = None
) -> response.RestResponseWithdrawal
```

Create a new withdrawal
See https://api-docs-v3.idex.io/[`withdraw`](#client.rest.authenticated.RestAuthenticatedClient.withdraw)-funds

<a id="client.rest.authenticated.RestAuthenticatedClient.get_withdrawal"></a>

#### get\_withdrawal

```python
def get_withdrawal(
        req: request.RestRequestFindWithdrawal
) -> response.RestResponseWithdrawal
```

Get a withdrawal
See https://api-docs-v3.idex.io/`get`-withdrawals

<a id="client.rest.authenticated.RestAuthenticatedClient.get_withdrawals"></a>

#### get\_withdrawals

```python
def get_withdrawals(
    req: request.RestRequestFindWithdrawals
) -> List[response.RestResponseWithdrawal]
```

Get multiple withdrawals
See https://api-docs-v3.idex.io/`get`-withdrawals

<a id="client.rest.authenticated.RestAuthenticatedClient.get_ws_token"></a>

#### get\_ws\_token

```python
def get_ws_token(nonce: str, wallet: str) -> str
```

Get multiple withdrawals
See https://api-docs-v3.idex.io/`get`-withdrawals

