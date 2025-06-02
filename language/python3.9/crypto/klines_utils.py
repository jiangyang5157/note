import json
import os
import pandas as pd
from typing import List, Any
from tzlocal import get_localzone

def save_klines_to_json(klines: List[List[Any]], filename: str) -> None:
    """Saves kline data to a JSON file.

    Args:
        klines: A list of kline data, where each kline is a list of data points.
        filename: The name of the output JSON file.
    """
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w") as f:
        json.dump(klines, f, indent=4)

    print(f"{len(klines)} Klines data saved to {filename}")


def read_klines_from_json(filename: str) -> List[List[Any]]:
    """Reads kline data from a local JSON file.

    Args:
        filename: The name of the JSON file containing kline data.

    Returns:
        A list of kline data, where each kline is a list of data points,
        or an empty list if the file is not found.
    """
    try:
        with open(filename, "r") as f:
            klines = json.load(f)

        print(f"{len(klines)} Klines data read from {filename}")
        return klines
    except FileNotFoundError:
        print(f"Error: file not found: {filename}")
        return []


def build_df_from_klines(klines: List[List[Any]]):
    df = pd.DataFrame(
        klines,
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
    df = df.drop("Ignore", axis=1)
    df["Open time"] = pd.to_datetime(df["Open time"], unit="ms")
    df["Close time"] = pd.to_datetime(df["Close time"], unit="ms")

    # Convert price and volume columns to float
    for col in [
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Quote asset volume",
        "Taker buy base asset volume",
        "Taker buy quote asset volume",
    ]:
        df[col] = df[col].astype(float)

    return df

def get_last_close_time_local(df: pd.DataFrame) -> str:
    """
    Gets the last close time from a DataFrame and converts it to the local timezone.

    Args:
        df (pd.DataFrame): The DataFrame containing 'Close time' column (assumed to be in UTC).

    Returns:
        str: The last close time formatted as a string in the local timezone.
    """

    last_close_time_utc = df['Close time'].max()
    local_timezone = get_localzone()
    last_close_time_local = last_close_time_utc.tz_localize('UTC').astimezone(local_timezone)
    return last_close_time_local.strftime('%Y-%m-%d %H:%M %Z%z')
