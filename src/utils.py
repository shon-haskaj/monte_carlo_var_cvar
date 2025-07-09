import yfinance as yf
import pandas as pd

def fetch_price_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Fetches historical data for `ticker` over `period` (e.g. "1y", "6mo").
    Returns a DataFrame indexed by Date with columns: Open, High, Low, Close, Adj Close, Volume.
    """
    df = yf.Ticker(ticker).history(period=period)
    df.index.name = "Date"
    return df

