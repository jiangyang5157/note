import os
import logging
logging.basicConfig(filename="lstm.log", level=logging.INFO)

import numpy as np
import tensorflow as tf
import pandas as pd
import klines_utils
import pickle
from ta import add_all_ta_features
from sklearn.preprocessing import MinMaxScaler
from typing import List, Tuple, Any

# Constants
THRESHOLD = 0.01
TIMESTEPS = 21

# Disable GPU (if needed)
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


def create_features(
    df: pd.DataFrame, threshold: float
) -> Tuple[pd.DataFrame, List[str], str]:
    """
    Creates features for the LSTM model, including technical indicators, lagged prices,
    time-based features, and the target variable.

    Args:
        df (pd.DataFrame): The input DataFrame containing kline data.
        threshold (float): The percentage change threshold for determining bullish/bearish.

    Returns:
        Tuple[pd.DataFrame, List[str], str]: A tuple containing:
            - The DataFrame with added features.
            - A list of numerical feature names.
            - The name of the target feature.
    """

    """
    ta_volume_adi
    ta_volume_obv
    ta_volume_cmf
    ta_volume_fi
    ta_volume_em
    ta_volume_sma_em
    ta_volume_vpt
    ta_volume_vwap
    ta_volume_mfi
    ta_volume_nvi
    ta_volatility_bbm
    ta_volatility_bbh
    ta_volatility_bbl
    ta_volatility_bbw
    ta_volatility_bbp
    ta_volatility_bbhi
    ta_volatility_bbli
    ta_volatility_kcc
    ta_volatility_kch
    ta_volatility_kcl
    ta_volatility_kcw
    ta_volatility_kcp
    ta_volatility_kchi
    ta_volatility_kcli
    ta_volatility_dcl
    ta_volatility_dch
    ta_volatility_dcm
    ta_volatility_dcw
    ta_volatility_dcp
    ta_volatility_atr
    ta_volatility_ui
    ta_trend_macd
    ta_trend_macd_signal
    ta_trend_macd_diff
    ta_trend_sma_fast
    ta_trend_sma_slow
    ta_trend_ema_fast
    ta_trend_ema_slow
    ta_trend_vortex_ind_pos
    ta_trend_vortex_ind_neg
    ta_trend_vortex_ind_diff
    ta_trend_trix
    ta_trend_mass_index
    ta_trend_dpo
    ta_trend_kst
    ta_trend_kst_sig
    ta_trend_kst_diff
    ta_trend_ichimoku_conv
    ta_trend_ichimoku_base
    ta_trend_ichimoku_a
    ta_trend_ichimoku_b
    ta_trend_stc
    ta_trend_adx
    ta_trend_adx_pos
    ta_trend_adx_neg
    ta_trend_cci
    ta_trend_visual_ichimoku_a
    ta_trend_visual_ichimoku_b
    ta_trend_aroon_up
    ta_trend_aroon_down
    ta_trend_aroon_ind
    ta_trend_psar_up
    ta_trend_psar_down
    ta_trend_psar_up_indicator
    ta_trend_psar_down_indicator
    ta_momentum_rsi
    ta_momentum_stoch_rsi
    ta_momentum_stoch_rsi_k
    ta_momentum_stoch_rsi_d
    ta_momentum_tsi
    ta_momentum_uo
    ta_momentum_stoch
    ta_momentum_stoch_signal
    ta_momentum_wr
    ta_momentum_ao
    ta_momentum_roc
    ta_momentum_ppo
    ta_momentum_ppo_signal
    ta_momentum_ppo_hist
    ta_momentum_pvo
    ta_momentum_pvo_signal
    ta_momentum_pvo_hist
    ta_momentum_kama
    ta_others_dr
    ta_others_dlr
    ta_others_cr
    """

    df = add_all_ta_features(
        df,
        open="Open",
        high="High",
        low="Low",
        close="Close",
        volume="Volume",
        colprefix="ta_",
        fillna=True,
    )

    # Target Variable (Bullish/Bearish)
    target_feature = "Target"
    df[target_feature] = np.where(
        df["Close"].shift(-1) > df["Close"] * (1 + threshold), 1, 0
    )

    # Get numerical feature names
    all_features = df.columns.tolist()
    numerical_features = [f for f in all_features if df[f].dtype != "datetime64[ns]"]

    # print(f"All features, includs target feature {target_feature}:")
    # for feature in numerical_features:
    #     print(feature)

    return df, numerical_features, target_feature


def prepare_data(
    df: pd.DataFrame,
    timesteps: int,
    features: List[str],
    target: str,
    scaler: MinMaxScaler,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Prepares data for the LSTM model, including normalization and windowing.

    Args:
        df (pd.DataFrame): The DataFrame with added features.
        timesteps (int): The number of past time steps to use.
        features (List[str]): The list of numerical feature names.
        target (str): The name of the target feature.
        scaler (MinMaxScaler): The scaler object to use for normalization.

    Returns:
        Tuple[np.ndarray, np.ndarray]: A tuple containing the input sequences (X) and target values (y).
    """

    # Drop rows with NaN values
    df.dropna(inplace=True)
    df[features] = scaler.fit_transform(df[features])

    X = []
    y = []
    for i in range(timesteps, len(df)):
        X.append(df[features].iloc[i - timesteps : i].to_numpy())
        y.append(df[target].iloc[i])

    return np.array(X), np.array(y)


def create_lstm_model(timesteps: int, features: List[str]) -> tf.keras.Model:
    """
    Creates and compiles the LSTM model.

    Args:
        timesteps (int): The number of past time steps to use.
        features (List[str]): The list of numerical feature names.

    Returns:
        tf.keras.Model: The compiled LSTM model.
    """

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(timesteps, len(features))),
            tf.keras.layers.LSTM(units=64, return_sequences=True),
            tf.keras.layers.LSTM(units=32),
            tf.keras.layers.Dense(units=1, activation="sigmoid"),
        ]
    )
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

    return model


def train_lstm_model(
    model: tf.keras.Model,
    X: np.ndarray,
    y: np.ndarray,
    train_size: float = 0.8,
    epochs: int = 100,
    batch_size: int = 256,
) -> Tuple[tf.keras.Model, float, float]:
    """
    Trains the LSTM model and returns the trained model, loss, and accuracy.

    Args:
        model (tf.keras.Model): The LSTM model to train.
        X (np.ndarray): The input sequences.
        y (np.ndarray): The target values.
        train_size (float, optional): The proportion of data for training. Defaults to 0.8.
            This represents the proportion of your dataset used for training the model.
            The remaining portion is typically used for validation (tuning hyperparameters) and testing (final evaluation).
            A common split is 80% for training, 10% for validation, and 10% for testing.
        epochs (int, optional): The number of training epochs. Defaults to 10.
            An epoch is one complete pass through your entire training dataset.
            The number of epochs determines how many times the model will see and learn from the training data.
            More epochs can lead to better learning,
            but too many can cause overfitting (where the model memorizes the training data but doesn't generalize well to new data).
            Begin with a moderate number, like 10 or 20.
            You can increase it if the model is underfitting (not learning enough)
            and decrease it if it's overfitting.
        batch_size (int, optional): The batch size for training. Defaults to 32.
            During training, the data is processed in batches.
            The batch_size determines how many samples are used in each training iteration.
            Smaller batch sizes can lead to more frequent weight updates and potentially faster convergence, but they can also make training more noisy.
            Larger batch sizes can be more computationally efficient but might require more memory.

    Returns:
        Tuple[tf.keras.Model, float, float]: A tuple containing the trained model, loss, and accuracy.
    """

    X_size = int(len(X) * train_size)
    y_size = int(len(y) * train_size)
    X_train, X_test = X[:X_size], X[X_size:]
    y_train, y_test = y[:y_size], y[y_size:]

    model.fit(
        X_train,
        y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_test, y_test),
    )
    loss, accuracy = model.evaluate(X_test, y_test)

    logging.info(f"Loss: {loss}, Accuracy: {accuracy} - epochs: {epochs}, batch_size: {batch_size}, train_size: {train_size}")

    return model, loss, accuracy


def train_model(data_filenames: List[str]) -> Tuple[tf.keras.Model, MinMaxScaler]:
    """
    Trains the LSTM model on the given data and returns the trained model and scaler.

    Args:
        data_filenames (List[str]): A list of filenames containing kline data.

    Returns:
        Tuple[tf.keras.Model, MinMaxScaler]: A tuple containing the trained model and the fitted scaler.
    """

    df = pd.DataFrame()
    for data_filename in data_filenames:
        klines = klines_utils.read_klines_from_json(data_filename)
        temp_df = klines_utils.build_df_from_klines(klines=klines)
        df = pd.concat([df, temp_df], ignore_index=True)

    scaler = MinMaxScaler()

    df, features, target_feature = create_features(df, THRESHOLD)
    X, y = prepare_data(df, TIMESTEPS, features, target_feature, scaler)
    model = create_lstm_model(TIMESTEPS, features)
    model, _, _ = train_lstm_model(model, X, y)

    return model, scaler


def predict_new_data(
    model: tf.keras.Model, scaler: MinMaxScaler, new_data_filename: str
) -> np.ndarray:
    """
    Loads new data, preprocesses it, and makes predictions using the trained model.

    Args:
        model (tf.keras.Model): The trained LSTM model.
        scaler (MinMaxScaler): The fitted scaler object.
        new_data_filename (str): The name of the JSON file containing new kline data.

    Returns:
        np.ndarray: The model's predictions.
    """

    new_klines = klines_utils.read_klines_from_json(new_data_filename)
    new_df = klines_utils.build_df_from_klines(klines=new_klines)

    new_df, features, _ = create_features(new_df, THRESHOLD)
    new_data_features = pd.DataFrame(
        new_df[features].tail(TIMESTEPS).values, columns=features
    )

    new_data = scaler.transform(new_data_features)
    new_data = new_data.reshape(1, TIMESTEPS, len(features))
    predictions = model.predict(new_data)

    logging.info(f"Predictions: {predictions} - {new_data_filename} - Last close time: {klines_utils.get_last_close_time_local(new_df)}")
    return predictions


def update_model(
    model: tf.keras.Model,
    scaler: MinMaxScaler,
    historical_data_filenames: List[str],
    new_data_filname: str,
) -> Tuple[tf.keras.Model, MinMaxScaler]:
    """
    Updates the model with new data and returns the updated model and scaler.

    Args:
        model (tf.keras.Model): The trained LSTM model.
        scaler (MinMaxScaler): The fitted scaler object.
        historical_data_filenames (List[str]): A list of filenames containing historical kline data.
        new_data_filname (str): The name ofthe JSON file containing new kline data.

    Returns:
        Tuple[tf.keras.Model, MinMaxScaler]: A tuple containing the updated model and the fitted scaler.
    """

    # Load historical data from multiple files
    historical_df = pd.DataFrame()
    for filename in historical_data_filenames:
        historical_klines = klines_utils.read_klines_from_json(filename)
        temp_df = klines_utils.build_df_from_klines(klines=historical_klines)
        historical_df = pd.concat([historical_df, temp_df], ignore_index=True)

    # Load new data
    new_klines = klines_utils.read_klines_from_json(new_data_filname)
    new_df = klines_utils.build_df_from_klines(klines=new_klines)

    # Combine data
    combined_df = pd.concat([historical_df, new_df], ignore_index=True)

    # Preprocess combined data
    combined_df, features, target_feature = create_features(combined_df, THRESHOLD)
    X, y = prepare_data(combined_df, TIMESTEPS, features, target_feature, scaler)

    # Retrain the model
    model, _, _ = train_lstm_model(model, X, y)

    return model, scaler


def save_model_and_scaler(
    model: tf.keras.Model,
    scaler: MinMaxScaler,
    model_filename: str,
    scaler_filename: str,
) -> None:
    """
    Saves the trained model and scaler to files.

    Args:
        model_filename (str): The filename for the model.
        scaler_filename (str): The filename for the scaler.
        model (tf.keras.Model, optional): The trained model. Defaults to None.
        scaler (MinMaxScaler, optional): The fitted scaler. Defaults to None.
    """
    if not model:
        logging.error("Error: Model is not provided for saving.")
        return
    if not scaler:
        logging.error("Error: Scaler is not provided for saving.")
        return

    try:
        os.makedirs(os.path.dirname(model_filename), exist_ok=True)
        model.save(model_filename)
        logging.info(f"Model saved to {model_filename}")
    except (OSError, pickle.PickleError) as e:
        logging.error(f"Error: saving model to {model_filename}: {e}")

    try:
        os.makedirs(os.path.dirname(scaler_filename), exist_ok=True)
        with open(scaler_filename, "wb") as file:
            pickle.dump(scaler, file)
        logging.info(f"Scaler saved to {scaler_filename}")
    except (OSError, pickle.PickleError) as e:
        logging.error(f"Error: saving scaler to {scaler_filename}: {e}")


def load_model_and_scaler(
    model_filename: str, scaler_filename: str
) -> Tuple[tf.keras.Model, MinMaxScaler]:
    """
    Loads the trained model and scaler from files.

    Args:
        model_filename (str): The filename of the saved model.
        scaler_filename (str): The filename of the saved scaler.

    Returns:
        Tuple[tf.keras.Model, MinMaxScaler]: A tuple containing the loaded model and scaler.
    """

    loaded_model = tf.keras.models.load_model(model_filename)
    logging.info(f"Model loaded from {model_filename}")

    with open(scaler_filename, "rb") as file:
        loaded_scaler = pickle.load(file)
    logging.info(f"Scaler loaded from {scaler_filename}")

    return loaded_model, loaded_scaler
