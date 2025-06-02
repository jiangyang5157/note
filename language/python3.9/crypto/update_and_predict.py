import argparse
import lstm_utils as lstm

if __name__ == "__main__":
    """Loads, updates, and makes predictions with the LSTM model."""

    parser = argparse.ArgumentParser(
        description="Update and predict with an LSTM model."
    )
    parser.add_argument(
        "new_data_filename", help="Path to the JSON file containing new kline data."
    )
    parser.add_argument(
        "-hd",
        "--historical_data_filenames",
        nargs="+",
        default=[
            "data/BTCUSDT_1d_15Aug2017_27Oct2024.json",
            "data/BTCUSDT_4h_14Aug2023_27Oct2024.json",
            "data/BTCUSDT_1h_05Mar2024_27Oct2024.json",
            "data/BTCUSDT_15m_06Sep2024_27Oct2024.json",
        ],
        help="Path(s) to the JSON file(s) containing historical kline data. Default: Uses the provided list.",
    )
    parser.add_argument(
        "-m",
        "--model_filename",
        default="model/BTCUSDT_model.h5",
        help="Filename for loading and saving the trained model. Default: model/BTCUSDT_model.h5",
    )
    parser.add_argument(
        "-s",
        "--scaler_filename",
        default="model/BTCUSDT_scaler.pkl",
        help="Filename for loading and saving the fitted scaler. Default: model/BTCUSDT_scaler.pkl",
    )
    args = parser.parse_args()

    NEW_DATA_FILENAME = args.new_data_filename
    HISTORICAL_DATA_FILENAMES = args.historical_data_filenames
    MODEL_FILENAME = args.model_filename
    SCALER_FILENAME = args.scaler_filename

    model, scaler = lstm.load_model_and_scaler(MODEL_FILENAME, SCALER_FILENAME)

    # Make predictions before updating (optional)
    predictions_before = lstm.predict_new_data(model, scaler, NEW_DATA_FILENAME)
    print(f"Predictions before update: {predictions_before}")

    updated_model, updated_scaler = lstm.update_model(
        model, scaler, HISTORICAL_DATA_FILENAMES, NEW_DATA_FILENAME
    )

    lstm.save_model_and_scaler(
        updated_model, updated_scaler, MODEL_FILENAME, SCALER_FILENAME
    )

    predictions_after = lstm.predict_new_data(
        updated_model, updated_scaler, NEW_DATA_FILENAME
    )
    print(f"Predictions after update: {predictions_after}")
