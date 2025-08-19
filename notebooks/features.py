import pandas as pd

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add hour, weekday, and month columns based on a 'datetime' column."""
    df = df.copy()
    dt = pd.to_datetime(df['datetime'])
    df['hour']     = dt.dt.hour
    df['weekday']  = dt.dt.dayofweek  # 0=Mon
    df['month']    = dt.dt.month
    return df
