import argparse
import binance_utils as binance
import datetime
import klines_utils

if __name__ == "__main__":
    """Downloads historical klines from Binance and saves them to a JSON file.
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

    parser = argparse.ArgumentParser(
        description="Download historical kline data from Binance."
    )
    parser.add_argument(
        "-s",
        "--symbol",
        default="BTCUSDT",
        help="Trading symbol (e.g., BTCUSDT). Default: BTCUSDT",
    )
    parser.add_argument(
        "-i",
        "--interval",
        default="1d",
        help="Kline interval (e.g., '5m', '1h', '1d', '1w'). Default: '1d'",
    )
    parser.add_argument(
        "-p",
        "--period",
        default="1 week ago UTC",
        help="Time period for historical data or a paticular day (e.g., '1 day ago UTC', '1 week ago UTC', 27Oct2023). Default: '1 week ago UTC'",
    )

    args = parser.parse_args()

    SYMBOL = args.symbol.upper()
    INTERVAL = args.interval
    PERIOD = args.period
    OUTPUT_FILE = f"data/{SYMBOL}_{INTERVAL}_{PERIOD.replace(' ', '_')}_{datetime.date.today().strftime('%d%b%Y')}.json"

    klines = binance.fetch_historical_klines(
        symbol=SYMBOL, interval=INTERVAL, period=PERIOD
    )

    klines_utils.save_klines_to_json(klines, OUTPUT_FILE)
