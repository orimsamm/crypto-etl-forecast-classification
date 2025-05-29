# transform_crypto_data.py
# This script fetches crypto data from CoinGecko and transforms it into a clean, diverse dataset
# Written by Samuel Orimogunje

import requests
import pandas as pd

# Step 1: Call the CoinGecko API to get top 100 coins
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
else:
    print(f"Error {response.status_code} - API call failed")
    exit()

# Step 2: Define and keep the fields I want for my diverse dataset
columns_to_keep = [
    'id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume',
    'price_change_percentage_24h', 'high_24h', 'low_24h', 'circulating_supply',
    'total_supply', 'ath', 'atl', 'market_cap_rank', 'last_updated'
]

df_cleaned = df[columns_to_keep].copy()

# Step 3: Rename the fields for clarity
df_cleaned.rename(columns={
    'id': 'coin_id',
    'symbol': 'coin_symbol',
    'name': 'coin_name',
    'current_price': 'price_usd',
    'market_cap': 'market_cap_usd',
    'total_volume': 'volume_24h_usd',
    'price_change_percentage_24h': 'change_pct_24h',
    'high_24h': 'high_24h_usd',
    'low_24h': 'low_24h_usd',
    'ath': 'all_time_high',
    'atl': 'all_time_low',
    'market_cap_rank': 'rank_market_cap'
}, inplace=True)

# Step 4: Round numeric values safely
round_cols = [
    'price_usd', 'market_cap_usd', 'volume_24h_usd', 'change_pct_24h',
    'high_24h_usd', 'low_24h_usd', 'circulating_supply',
    'total_supply', 'all_time_high', 'all_time_low'
]

for col in round_cols:
    if col in df_cleaned.columns:
        df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce').round(2)

# Step 5: Export the cleaned data to CSV
df_cleaned.to_csv("cleaned_crypto_data.csv", index=False)
print("✅ Done! Saved: cleaned_crypto_data.csv")
