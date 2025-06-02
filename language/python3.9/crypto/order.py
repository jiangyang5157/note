import argparse
import binance_utils as binance
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox

# Global variables to store data and chart objects
order_book_data = None
large_buy_orders = None
large_sell_orders = None
fig = None
ax = None
symbol_textbox = None # For the symbol input text field


def fetch_and_process_data(symbol):
    """Fetches order book data and processes large orders."""
    global order_book_data, large_buy_orders, large_sell_orders
    order_book_data = binance.fetch_order_book(symbol=symbol, limit=5000)
    large_buy_orders, large_sell_orders = binance.get_large_orders_from_order_book(
        order_book_data, 500000
    )


def plot_chart(ax, symbol):
    """Plots the order book depth chart with highlighted large orders."""
    ax.clear()  # Clear the previous plot

    # Extract bids and asks into DataFrames
    bids = pd.DataFrame(order_book_data["bids"], columns=["price", "quantity"]).astype(
        float
    )
    asks = pd.DataFrame(order_book_data["asks"], columns=["price", "quantity"]).astype(
        float
    )

    # Plot buy and sell orders
    ax.plot(bids["quantity"], bids["price"], color="g", label="Buy Orders")
    ax.plot(asks["quantity"], asks["price"], color="r", label="Sell Orders")

    # Highlight large orders (use a loop for efficiency)
    for orders, color, marker in [
        (large_buy_orders, "green", "o"),
        (large_sell_orders, "red", "o"),
    ]:
        for start, end, qty in orders:
            ax.scatter(
                qty,
                (start + end) / 2,
                marker=marker,
                s=40,
                color=color,
                edgecolors="black",
            )

    # Set chart labels and title
    ax.set_xlabel("Asset Quantity")
    ax.set_ylabel("Price")
    ax.set_title(f"{symbol} Orders")
    ax.legend()


def update_chart(event):
    """Updates the chart with new order book data."""
    global symbol_textbox # Access the global textbox
    current_symbol = symbol_textbox.text.upper() # Get symbol from textbox
    print("Reloading chart...")
    fetch_and_process_data(current_symbol)
    plot_chart(ax, current_symbol) # Pass the current symbol to plot_chart
    fig.canvas.draw_idle()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze cryptocurrency order book.")
    parser.add_argument(
        "-s",
        "--symbol",
        default="BTCUSDT",
        help="Trading symbol (e.g., BTCUSDT). Default: BTCUSDT",
    )
    args = parser.parse_args()

    SYMBOL = args.symbol.upper()

    # Initial plot setup
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(bottom=0.1) # Adjust bottom to make space for widgets

    fetch_and_process_data(SYMBOL)
    plot_chart(ax, SYMBOL)

    # Add a TextBox for symbol input
    ax_textbox = plt.axes([0.15, 0.01, 0.2, 0.04]) # [left, bottom, width, height]
    symbol_textbox = TextBox(ax_textbox, "Symbol", initial=SYMBOL)
    # We don't need a submit function for the textbox itself,
    # as the reload button will trigger the update.

    # Add a reload button
    ax_reload = plt.axes([0.01, 0.01, 0.1, 0.04]) # Adjusted position
    reload_button = Button(ax_reload, "Reload")
    reload_button.on_clicked(
        update_chart # The update_chart function will get the symbol from the textbox
    )

    # Fullscreen mode
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.show()
