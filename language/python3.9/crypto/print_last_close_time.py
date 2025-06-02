import argparse
import klines_utils

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Print last close time from kline data"
    )
    parser.add_argument(
        "data_filename", help="Path to the JSON file containing the kline data."
    )
    args = parser.parse_args()

    DATA_FILENAME = args.data_filename

    klines = klines_utils.read_klines_from_json(DATA_FILENAME)
    df = klines_utils.build_df_from_klines(klines=klines)

    print(f"{DATA_FILENAME} - Last close time: {klines_utils.get_last_close_time_local(df)}")
