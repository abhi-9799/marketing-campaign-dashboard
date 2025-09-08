from google.cloud import bigquery
import pandas as pd
import numpy as np

# Authenticate
client = bigquery.Client.from_service_account_json("config.json")

# Load SQL
with open("sql/roi_trend.sql", "r") as f:
    query = f.read()

# Run query
df = client.query(query).to_dataframe()

# --- Handle missing values ---
df["sessions"] = df["sessions"].fillna(0)
df["transactions"] = df["transactions"].fillna(0)
df["revenue_usd"] = df["revenue_usd"].fillna(0)
df["clicks"] = df["clicks"].fillna(0)

# --- KPIs ---
df["CTR"] = df["clicks"] / df["sessions"].replace(0, pd.NA)
df["ConversionRate"] = df["transactions"] / df["sessions"].replace(0, pd.NA)

# --- Simulated Ad Spend ---
np.random.seed(42)
df["ad_cost_usd"] = df["clicks"] * np.random.uniform(0.2, 0.8, len(df))

# CPC & ROI
df["CPC"] = df["ad_cost_usd"] / df["clicks"].replace(0, pd.NA)
df["ROI"] = (df["revenue_usd"] - df["ad_cost_usd"]) / df["ad_cost_usd"]

# Drop rows where everything is 0
df = df[(df["sessions"] > 0) | (df["revenue_usd"] > 0) | (df["clicks"] > 0)]

# Save to CSV
df.to_csv("data/roi_trend.csv", index=False)

print("ROI trend data cleaned and saved to data/roi_trend.csv")
print(df.head(10))
