import pandas as pd

def preprocess_data(df, date_column: str):
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.dropna()
    return df