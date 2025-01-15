from src.data.load_data import load_data
from src.data.preprocess import preprocess_data
from src.features.build_features import create_lagged_features
from src.models.train_model import train_model
from src.models.evaluate_model import evaluate_model
from src.models.predict import predict_future
from src.utils.config import CONFIG
from src.utils.logging import setup_logging

if __name__ == "__main__":
    logger = setup_logging()

    # Load the data
    query = CONFIG["data_query"]
    logger.info("Loading data...")
    data = load_data(query)
    logger.info("Data loaded successfully.")

    # Preprocess the data
    logger.info("Preprocessing data...")
    preprocessed_data = preprocess_data(data, CONFIG["date_column"])
    logger.info("Data preprocessed successfully.")

    # Build features
    logger.info("Building features...")
    engineered_data = create_lagged_features(preprocessed_data, CONFIG["target_column"], CONFIG["lags"])
    logger.info("Features built successfully.")

    # Train the model
    logger.info("Training model...")
    model, metrics = train_model(engineered_data, CONFIG["lags"], CONFIG["n_forecasts"], CONFIG["quantiles"])
    logger.info("Model trained successfully.")

    # Evaluate the model
    logger.info("Evaluating model...")
    actuals = engineered_data[CONFIG["target_column"]][-CONFIG["n_forecasts"]:]
    forecast = predict_future(model, engineered_data, CONFIG["n_forecasts"])
    predicted = forecast["yhat1"][-CONFIG["n_forecasts"]:]
    rmse = evaluate_model(actuals, predicted)
    logger.info(f"Model evaluation complete. RMSE: {rmse}")

    # Predict using the model
    logger.info("Making predictions...")
    future_forecast = predict_future(model, engineered_data, CONFIG["n_forecasts"])
    logger.info("Predictions complete.")

    print("Future Forecast:")
    print(future_forecast.tail())