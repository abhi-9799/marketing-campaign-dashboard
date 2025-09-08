from google.cloud import bigquery
import pandas as pd
import numpy as np

# Authenticate
client = bigquery.Client.from_service_account_json("config.json")

# Load query
with open("sql/campaign_performance.sql", "r") as f:
    query = f.read()

# Run query
df = client.query(query).to_dataframe()

# Compute KPIs
df["CTR"] = df["clicks"] / df["sessions"]
df["ConversionRate"] = df["transactions"] / df["sessions"]

# --- Add Simulated Ad Spend ---
# Let's assume campaigns spend between $0.2 and $0.8 per click
np.random.seed(42)  # reproducible random values
df["ad_cost_usd"] = df["clicks"].fillna(0) * np.random.uniform(0.2, 0.8, len(df))

# Add CPC and ROI
df["CPC"] = df["ad_cost_usd"] / df["clicks"].replace(0, np.nan)
df["ROI"] = (df["revenue_usd"] - df["ad_cost_usd"]) / df["ad_cost_usd"]

# Save results to CSV
df.to_csv("data/campaign_performance.csv", index=False)

print("Query complete. Results saved to data/campaign_performance.csv")
print(df.head())
