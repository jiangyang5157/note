import argparse
import binance_utils as binance
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, TextBox

# Global variables
fig = None
ax = None
watchlist_textbox = None
large_orders_summary = [] # To store summary data for plotting

def fetch_and_process_data(symbols_to_check, threshold):
    """
    Fetches order book data for symbols and identifies the total value of large order levels.
    """
    global large_orders_summary
    large_orders_summary = []
    print(f"Fetching data for symbols: {', '.join(symbols_to_check)} with threshold: {threshold:,.0f}")

    for symbol in symbols_to_check:
        print(f"Processing {symbol}...")
        order_book = binance.fetch_order_book(symbol=symbol, limit=5000) # Deep order book

        if not order_book or "bids" not in order_book or "asks" not in order_book:
            print(f"Could not fetch or parse order book for {symbol}. Skipping.")
            continue

        total_large_buy_value = 0
        for price_str, qty_str in order_book["bids"]:
            price = float(price_str)
            qty = float(qty_str)
            level_value = price * qty
            if level_value >= threshold:
                total_large_buy_value += level_value

        total_large_sell_value = 0
        for price_str, qty_str in order_book["asks"]:
            price = float(price_str)
            qty = float(qty_str)
            level_value = price * qty
            if level_value >= threshold:
                total_large_sell_value += level_value
        
        if total_large_buy_value > 0 or total_large_sell_value > 0:
            large_orders_summary.append({
                "symbol": symbol,
                "total_large_buy_value": total_large_buy_value,
                "total_large_sell_value": total_large_sell_value,
            })
            print(f"  {symbol}: Large Buys Value: {total_large_buy_value:,.0f}, Large Sells Value: {total_large_sell_value:,.0f}")
        else:
            print(f"  {symbol}: No large orders found above threshold.")
    
    # Sort by symbol name for consistent plotting order
    large_orders_summary.sort(key=lambda x: x['symbol'])


def plot_chart(ax_main, threshold):
    """
    Plots a bar chart summarizing large order values for symbols.
    """
    ax_main.clear()

    if not large_orders_summary:
        ax_main.text(0.5, 0.5, "No large orders found for the current watchlist and threshold.",
                     horizontalalignment='center', verticalalignment='center', transform=ax_main.transAxes)
        ax_main.set_title(f"Large Order Alert (Threshold: {threshold:,.0f} USDT)")
        ax_main.set_xticks([])
        ax_main.set_yticks([])
        return

    symbols = [item['symbol'] for item in large_orders_summary]
    buy_values = [item['total_large_buy_value'] for item in large_orders_summary]
    sell_values = [item['total_large_sell_value'] for item in large_orders_summary]

    x = np.arange(len(symbols))  # the label locations
    width = 0.35  # the width of the bars

    rects1 = ax_main.bar(x - width/2, buy_values, width, label='Large Buy Value', color='green')
    rects2 = ax_main.bar(x + width/2, sell_values, width, label='Large Sell Value', color='red')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax_main.set_ylabel('Total Value (USDT)')
    ax_main.set_title(f"Large Order Alert (Threshold: {threshold:,.0f} USDT)")
    ax_main.set_xticks(x)
    ax_main.set_xticklabels(symbols, rotation=45, ha="right")
    ax_main.legend()

    ax_main.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f'{val:,.0f}'))

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            if height > 0: # Only label if value is > 0
                ax_main.annotate(f'{height:,.0f}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom', fontsize=8, rotation=45)

    autolabel(rects1)
    autolabel(rects2)

    ax_main.grid(True, axis='y', linestyle='--', alpha=0.7)
    fig.tight_layout(rect=[0, 0.1, 1, 1]) # Adjust layout to make space for x-labels and bottom widgets


def update_chart(event, threshold):
    """
    Handles the reload button click.
    Fetches new data based on the watchlist_textbox and redraws the chart.
    """
    global watchlist_textbox
    current_watchlist_str = watchlist_textbox.text
    current_watchlist = [symbol.strip().upper() for symbol in current_watchlist_str.split(',') if symbol.strip()]
    print("Reloading chart...")
    fetch_and_process_data(current_watchlist, threshold)
    plot_chart(ax, threshold) # Pass the current symbol to plot_chart
    fig.canvas.draw_idle()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Detect and visualize large order levels for a list of symbols."
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=float,
        default=500000,
        help="Asset threshold for defining a large order level (in quote asset value, e.g., USDT). Default: 500000",
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

    WATCH_LIST = [symbol.upper() for symbol in args.watchlist]
    THRESHOLD = args.threshold

    # Initial Matplotlib setup
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.2) # Adjust bottom to make space for widgets

    # Fetch initial data and plot
    fetch_and_process_data(WATCH_LIST, THRESHOLD)
    plot_chart(ax, THRESHOLD)

    # --- UI Widgets ---
    # Reload Button
    ax_reload_left = 0.02
    ax_reload_bottom = 0.05 # Position from bottom of the figure
    ax_reload_width = 0.1
    ax_reload_height = 0.04
    
    reload_ax = plt.axes([ax_reload_left, ax_reload_bottom, ax_reload_width, ax_reload_height])
    reload_button = Button(reload_ax, "Reload")
    reload_button.on_clicked(
        lambda event: update_chart(event, THRESHOLD) # The update_chart function will get the symbol from the textbox
    )

    # Watchlist TextBox
    ax_watchlist_left = ax_reload_left + ax_reload_width + 0.01
    ax_watchlist_bottom = ax_reload_bottom 
    # Calculate width to fill remaining space, considering a right margin
    ax_watchlist_width = 0.98 - ax_watchlist_left 
    ax_watchlist_height = ax_reload_height

    watchlist_ax = plt.axes([ax_watchlist_left, ax_watchlist_bottom, ax_watchlist_width, ax_watchlist_height])
    initial_watchlist_str = ", ".join(WATCH_LIST)
    watchlist_textbox = TextBox(watchlist_ax, "", initial=initial_watchlist_str, textalignment="left")
    
    # Fullscreen mode
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()
