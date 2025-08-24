# features.py
import pandas as pd

def add_time_features(df):
    df = df.copy()
    dt = pd.to_datetime(df["datetime"])
    df["hour"]     = dt.dt.hour
    df["weekday"]  = dt.dt.dayofweek      # 0=Mon
    df["month"]    = dt.dt.month
    df["is_weekend"] = df["weekday"].isin([5,6]).astype(int)
    return df

def add_weather_buckets(df):
    df = df.copy()
    mapping = {1: "Clear", 2: "Mist", 3: "Light Rain", 4: "Heavy Rain"}
    df["weather_bin"] = df["weather"].map(mapping)
    return df

def add_rolling_mean(df, hours=3):
    df = df.sort_values("datetime").copy()
    df[f"count_roll_{hours}h"] = df["count"].rolling(hours).mean()
    return df
