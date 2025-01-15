def predict_future(model, df, periods: int):
    future = model.make_future_dataframe(df, periods=periods)
    forecast = model.predict(future)
    return forecast