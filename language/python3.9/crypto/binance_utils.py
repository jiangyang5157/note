import binance
import time
import pandas as pd
from typing import Dict, List, Tuple
from tqdm import tqdm

# https://github.com/sammchardy/python-binance/blob/master/binance/client.py
client = binance.Client()

def fetch_all_symbols() -> List[Dict]:
    """Fetches all trading symbols from the Binance API.

    Returns:
        List[Dict]: A list of dictionaries, where each dictionary represents a trading symbol.
    """
    try:
        return client.get_exchange_info()["symbols"]
    except binance.exceptions.BinanceAPIException as e:
        print(f"Error: fetching symbols: {e}")
        return []


def fetch_usdt_symbols() -> List[str]:
    """Fetches and returns a sorted list of USDT trading pairs from Binance.

    Returns:
        List[str]: A sorted list of USDT trading pairs.
    """
    symbols = fetch_all_symbols()
    return filter_usdt_symbols(symbols)


def filter_usdt_symbols(symbols: List[Dict]) -> List[str]:
    """Filters a list of symbols, keeping only those ending with 'USDT'.

    Args:
        symbols (List[Dict]): A list of symbol dictionaries.

    Returns:
        List[str]: A sorted list of USDT symbols.
    """
    return sorted(
        [
            symbol_data["symbol"]
            for symbol_data in symbols
            if symbol_data["symbol"].endswith("USDT")
        ]
    )


def fetch_historical_klines(symbol: Dict, interval: str, period: str) -> List:
    """Fetches historical kline data for a given symbol.

    Args:
        symbol (str): The trading symbol.
        interval (str): The kline interval (e.g., '1m', '15m', '1h', '1d', '1w').
        period (str): The time period for historical data (e.g., '1 day ago UTC').

    Returns:
        List: A list of kline data.
        [
            [
                1499040000000,      # Open time (in milliseconds since Unix epoch)
                "0.01634790",       # Open
                "0.80000000",       # High
                "0.01575800",       # Low
                "0.01577100",       # Close
                "148976.11427815",  # This represents the total quantity of the base asset traded within that specific kline (candlestick) timeframe
                1499644799999,      # Close time (in milliseconds since Unix epoch)
                "2434.19055334",    # This represents the total quantity of the quote asset traded within the kline's timeframe
                308,                # The total number of trades that occurred during the kline interval.
                "1756.87402397",    # This is the volume of the base asset traded by buyers who "took" liquidity from the order book.
                "28.46694368",      # This is the volume of the quote asset traded by buyers who "took" liquidity
                "17928899.62484339" # Can be ignored
            ]
        ]
    """
    try:
        ret = client.get_historical_klines(symbol, interval, period)

        # Rate limiting with exponential backoff
        wait_time = 1
        while int(client.response.headers["x-mbx-used-weight-1m"]) > 1_000:
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)
            wait_time *= 2  # Exponential backoff

        return ret
    except binance.exceptions.BinanceAPIException as e:
        print(f"Error: fetching kline data for {symbol}: {e}")
        return []


def fetch_multiple_klines(
    symbols: List[str], interval: str, period: str
) -> Dict[str, List]:
    """Fetches historical kline data for multiple symbols.

    Args:
        symbols (List[str]): A list of trading symbols.
        interval (str): The kline interval.
        period (str): The time period for historical data.

    Returns:
        Dict[str, List]: A dictionary where keys are symbols and values are lists of kline data.
    """
    ret = {}

    for symbol in tqdm(symbols):
        ret[symbol] = fetch_historical_klines(symbol, interval, period)

    return ret


def fetch_order_book(symbol: str, limit=1000) -> Dict:
    """Fetches the order book for the given symbol(s).

    Args:
        symbol (str): The trading symbol.
        limit (int, optional): The maximum number of orders to return.

    Returns:
        Dict: The order book data.
        {
            "lastUpdateId": 1027024,
            "bids": [              # Buy
                [
                    "4.00000000",  # PRICE
                    "431.00000000" # QTY
                ]
            ],
            "asks": [              # Sell
                [
                    "4.00000200",
                    "12.00000000"
                ]
            ]
        }
    """
    try:
        return client.get_order_book(symbol=symbol, limit=limit)
    except binance.exceptions.BinanceAPIException as e:
        print(f"Error: fetching order book for {symbol}: {e}")
        return {}  # Return an empty dictionary to indicate an error


def get_large_orders_from_order_book(
    order_book: Dict, asset_threshold: float
) -> Tuple[List[Tuple[float, float, float]], List[Tuple[float, float, float]]]:
    """Analyzes order book data to identify large buy and sell order ranges with quantities.

    Args:
        order_book (Dict): Order book data containing 'bids' and 'asks' dictionaries.
        asset_threshold (float): Threshold for large orders (in quote asset value).

    Returns:
        Tuple[List[Tuple[float, float, float]], List[Tuple[float, float, float]]]: A tuple containing two lists:
            - large_buy_orders: List of large buy orders as tuples (start_price, end_price, qty).
            - large_sell_orders: List of large sell orders as tuples (start_price, end_price, qty).
    """

    large_buy_orders = []
    large_sell_orders = []

    # Analyze buy orders
    start_price = None
    total_qty = 0
    for price, qty in order_book["bids"]:
        price = float(price)
        qty = float(qty)
        asset_qty = price * qty
        if asset_qty >= asset_threshold:
            if start_price is None:
                start_price = price
            total_qty += qty
        else:
            if start_price is not None:
                large_buy_orders.append((start_price, price, total_qty))
                start_price = None
                total_qty = 0

    # Handle the last interval for buy orders
    if start_price is not None:
        large_buy_orders.append((start_price, float("*"), total_qty))

    # Analyze sell orders (similar to buy orders)
    start_price = None
    total_qty = 0
    for price, qty in order_book["asks"]:
        price = float(price)
        qty = float(qty)
        asset_qty = price * qty
        if asset_qty >= asset_threshold:
            if start_price is None:
                start_price = price
            total_qty += qty
        else:
            if start_price is not None:
                large_sell_orders.append((start_price, price, total_qty))
                start_price = None
                total_qty = 0

    # Handle the last interval for sell orders
    if start_price is not None:
        large_sell_orders.append((start_price, float("*"), total_qty))

    # Sort by qty in descending order
    large_buy_orders.sort(key=lambda x: x[2], reverse=True)
    large_sell_orders.sort(key=lambda x: x[2], reverse=True)

    print("Large buy orders:")
    for start_price, end_price, qty in large_buy_orders:
        print(f"  {start_price} - {end_price}, Quantity: {qty}")

    print("Large sell orders:")
    for start_price, end_price, qty in large_sell_orders:
        print(f"  {start_price} - {end_price}, Quantity: {qty}")

    return large_buy_orders, large_sell_orders


def get_most_volatile_symbols_with_fluctuation(
    klines: dict, volatility_threshold: float, top_n: int = 10
) -> list:
    """
    Analyzes kline data to find the most volatile symbols within the target period,
    returning their price fluctuations.

    Args:
        klines: A dictionary where keys are symbols and values are lists of kline data.
        volatility_threshold: Minimum percentage price change within the target period to be considered volatile.
        top_n: The number of most volatile symbols to return.

    Returns:
        A list of dictionaries, each containing:
            - 'symbol': The symbol.
            - 'price_change': The percentage price change within the target period.
            - 'fluctuations': A list of price fluctuations for each kline within the target period.
    """

    symbol_data = []

    for symbol, kline_data in klines.items():
        df = pd.DataFrame(
            kline_data,
            columns=[
                "Open time",
                "Open",
                "High",
                "Low",
                "Close",
                "Volume",
                "Close time",
                "Quote asset volume",
                "Number of trades",
                "Taker buy base asset volume",
                "Taker buy quote asset volume",
                "Ignore",
            ],
        )
        df["Open time"] = pd.to_datetime(df["Open time"], unit="ms")
        df["Close time"] = pd.to_datetime(df["Close time"], unit="ms")
        df["Close"] = df["Close"].astype(float)

        if len(df["Close"]) <= 1:
            print(f"Warning: Skipping symbol {symbol} due to insufficient kline data.")
            continue

        # Calculate price change within the target period
        price_change = (df["Close"].iloc[-1] - df["Close"].iloc[0]) / df["Close"].iloc[
            0
        ]
        price_change_percentage = "{:.0%}".format(price_change)
        print(f"{symbol}: price changed {price_change_percentage}")

        if abs(price_change) < volatility_threshold:
            continue

        fluctuations = df["Close"].pct_change().dropna().tolist()

        symbol_data.append(
            {
                "symbol": symbol,
                "price_change": price_change,
                "fluctuations": fluctuations,
            }
        )

    return sorted(symbol_data, key=lambda x: abs(x["price_change"]), reverse=True)[
        :top_n
    ]
