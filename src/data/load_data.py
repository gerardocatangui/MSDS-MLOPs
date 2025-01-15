import pandas as pd
from pyspark.sql import SparkSession

def load_data(query: str):
    spark = SparkSession.builder.appName("EnergyProductionForecast").getOrCreate()
    df = spark.sql(query).toPandas()
    return df