import numpy as np
import pandas as pd

def compute_log_returns(csv_path: str) -> pd.DataFrame:
    """
    Reads CSV of adjusted close prices, computes daily log returns,
    and returns a DataFrame with columns ['Adj Close', 'log_ret'].
    """
    df = pd.read_csv(csv_path, parse_dates=["Date"], index_col="Date")
    df = df[["Adj Close"]].dropna()
    df["log_ret"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    return df.dropna()

