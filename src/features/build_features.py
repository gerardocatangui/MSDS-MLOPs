def create_lagged_features(df, column: str, lags: int):
    for lag in range(1, lags + 1):
        df[f"{column}_lag_{lag}"] = df[column].shift(lag)
    return df.dropna()