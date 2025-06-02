import argparse
import lstm_utils as lstm

if __name__ == "__main__":
    """Trains the initial LSTM model and saves it with the scaler."""

    parser = argparse.ArgumentParser(description="Train an LSTM model.")
    parser.add_argument(
        "--data_filenames",
        nargs="+",
        default=[
            "data/BTCUSDT_1d_15Aug2017_27Oct2024.json",
            "data/BTCUSDT_4h_14Aug2023_27Oct2024.json",
            "data/BTCUSDT_1h_05Mar2024_27Oct2024.json",
        ],
        help="Path(s) to the JSON file(s) containing kline data. Default: Uses the provided list.",
    )
    parser.add_argument(
        "-m",
        "--model_filename",
        default="model/BTCUSDT_model.h5",
        help="Filename for saving the trained model. Default: model/BTCUSDT_model.h5",
    )
    parser.add_argument(
        "-s",
        "--scaler_filename",
        default="model/BTCUSDT_scaler.pkl",
        help="Filename for saving the fitted scaler. Default: model/BTCUSDT_scaler.pkl",
    )
    args = parser.parse_args()

    DATA_FILENAMES = args.data_filenames
    MODEL_FILENAME = args.model_filename
    SCALER_FILENAME = args.scaler_filename

    model, scaler = lstm.train_model(DATA_FILENAMES)
    lstm.save_model_and_scaler(model, scaler, MODEL_FILENAME, SCALER_FILENAME)
