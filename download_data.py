# src/scripts/download_data.py
import os
from src.utils import fetch_price_data

# 1. Fetch 1 year of daily SPY data
ticker = "SPY"
df = fetch_price_data(ticker, period="1y")

# 2. Ensure data directory exists
os.makedirs("data", exist_ok=True)

# 3. Write to CSV
out_path = f"data/{ticker}_raw.csv"
df.to_csv(out_path)

print(f"✔️  Saved {len(df)} rows to {out_path}")

