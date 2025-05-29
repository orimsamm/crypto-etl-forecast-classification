# CoinGecko Crypto ETL - Step 1: Extract Data
# Written by Samuel Orimogunje

import requests  # I’m using requests to call the CoinGecko API
import pandas as pd  # I’ll use pandas to structure the JSON response into a DataFrame

# CoinGecko endpoint for market data
url = "https://api.coingecko.com/api/v3/coins/markets"

# These parameters tell the API to give me the top 100 coins by market cap in USD
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 100,
    'page': 1,
    'sparkline': False
}

# Make the GET request to fetch the data
response = requests.get(url, params=params)

# Check if the request was successful before moving on
if response.status_code == 200:
    data = response.json()  # Convert the JSON response to a Python list
    df = pd.DataFrame(data)  # Convert that list into a DataFrame for analysis
    
    # Just show a preview of the main fields I care about
    print(df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume']].head())
else:
    print(f"Error {response.status_code} - Couldn’t retrieve data from CoinGecko")
