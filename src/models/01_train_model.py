def train_model(df, n_lags: int, n_forecasts: int, quantiles: list):
    model = NeuralProphet(n_lags=n_lags, n_forecasts=n_forecasts, quantiles=quantiles)
    metrics = model.fit(df, freq='H', valid_p=0.2)
    return model, metrics