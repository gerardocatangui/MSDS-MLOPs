import pandas as pd

def load_data(df: str):
    df = pd.read_csv("../data/data.csv")
    return df