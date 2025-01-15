CONFIG = {
    "data_query": "SELECT * FROM plant_ops.mao_forecast.gesq_accuweather ORDER BY CALENDAR_DATE",
    "date_column": "CALENDAR_DATE",
    "target_column": "target_column",
    "lags": 15,
    "n_forecasts": 15,
    "quantiles": [0.05, 0.5, 0.95],
}