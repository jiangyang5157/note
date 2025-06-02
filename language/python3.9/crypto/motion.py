import argparse
import binance_utils as binance
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.widgets import Button, TextBox

# Global variables to store data and chart objects
klines = None
most_volatile = None
fig = None
ax = None
watchlist_textbox = None # For the watchlist input text field

def fetch_and_process_data(interval, period, threshold, watch_list=None):
    """Fetches kline data and identifies most volatile symbols."""
    global klines, most_volatile

    symbols = watch_list if watch_list else binance.fetch_usdt_symbols()
    klines = binance.fetch_multiple_klines(
        symbols=symbols, interval=interval, period=period
    )
    most_volatile = binance.get_most_volatile_symbols_with_fluctuation(
        klines,
        threshold,
    )

def plot_chart(ax, period, threshold):
    """Plots the cumulative price fluctuation chart."""
    ax.clear()  # Clear the previous plot

    for symbol_data in most_volatile:
        symbol = symbol_data["symbol"]
        fluctuations = symbol_data["fluctuations"]
        times = [pd.to_datetime(kline[0], unit="ms") for kline in klines[symbol]][1:]
        cumulative_fluctuations = pd.Series(fluctuations).cumsum().tolist()
        (line,) = ax.plot(times, cumulative_fluctuations, label=symbol)
        line_color = line.get_color()
        ax.text(
            times[-1],
            cumulative_fluctuations[-1],
            f"  {symbol}",
            va="center",
            color=line_color,
        )

    # ax.set_title(f"Price Fluctuations Threshold {"{:.0%}".format(VOLATILITY_THRESHOLD)}")
    ax.set_title(f"Price Fluctuations Threshold {{{threshold:.0%}}}")
    ax.set_xlabel(f"Time ({period})")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y%m%d %H:%M"))
    ax.set_ylabel("Cumulative Price Fluctuation")
    ax.yaxis.set_major_formatter("{:.0%}".format)
    ax.legend(loc="upper left", bbox_to_anchor=(0, 1), ncol=2, fontsize="small")


def update_chart(event, interval, period, threshold):
    """Updates the chart with the latest data."""
    global watchlist_textbox # Access the global textbox
    print("Reloading chart...")
    # Get symbols from textbox, split by newline, strip whitespace, and convert to uppercase
    current_watchlist = [symbol.strip().upper() for symbol in watchlist_textbox.text.split(',') if symbol.strip()]
    fetch_and_process_data(interval, period, threshold, current_watchlist)
    plot_chart(ax, period, threshold)
    fig.canvas.draw_idle()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze cryptocurrency price fluctuations."
    )
    parser.add_argument(
        "-i",
        "--interval",
        default="15m",
        help="Kline interval (e.g., '5m', '15m', '1h', '1d'). Default: '15m'",
    )
    parser.add_argument(
        "-p",
        "--period",
        default="1w",
        help="Time period for historical data (e.g., '1d', '1w', '1M'). Default: '1w'",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default="0.00",
        help="Volatility threshold (e.g., 0.01 for 1%). Default: 0.00",
    )
    parser.add_argument(
        "-w",
        "--watchlist",
        nargs="+",
        default=[
            "BTCUSDT",

            "BNBUSDT",
            "ETHUSDT",
            "SOLUSDT",
        ],
        help="Space-separated list of symbols to watch (e.g., BTCUSDT ETHUSDT). Default: BTCUSDT ETHUSDT BNBUSDT SOLUSDT",
    )
    args = parser.parse_args()

    INTERVAL = args.interval
    PERIOD = args.period
    THRESHOLD = args.threshold
    WATCH_LIST = [symbol.upper() for symbol in args.watchlist]

    # Initial setup
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.2) # Adjust bottom to make space for widgets

    fetch_and_process_data(INTERVAL, PERIOD, THRESHOLD, WATCH_LIST)
    plot_chart(ax, PERIOD, THRESHOLD)

    # Add a reload button
    reload_button_ax_left = 0.02
    reload_button_ax_bottom = 0.05
    reload_button_ax_width = 0.1
    reload_button_ax_height = 0.04

    ax_reload_left = 0.01
    ax_reload_bottom = 0.01
    ax_reload_width = 0.1
    ax_reload_height = 0.04

    ax_reload = plt.axes([ax_reload_left, ax_reload_bottom, ax_reload_width, ax_reload_height])
    reload_button = Button(ax_reload, "Reload")
    reload_button.on_clicked(
        lambda event: update_chart(event, INTERVAL, PERIOD, THRESHOLD)
    )

    # Add a TextBox for watchlist input
    ax_watchlist_left = ax_reload_left + ax_reload_width + 0.01
    ax_watchlist_bottom = ax_reload_bottom
    ax_watchlist_width = 1 - ax_reload_left  - ax_watchlist_left
    ax_watchlist_height = ax_reload_height
    ax_watchlist = plt.axes([ax_watchlist_left, ax_watchlist_bottom, ax_watchlist_width, ax_watchlist_height]) # [left, bottom, width, height]
    initial_watchlist = ", ".join(WATCH_LIST) # Use comma and space as separator
    watchlist_textbox = TextBox(ax_watchlist, "", initial=initial_watchlist)

    # Fullscreen mode
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()
