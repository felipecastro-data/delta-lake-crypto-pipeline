import requests
import pandas as pd

def get_market_data(coin_id="bitcoin", currency="usd", days=30):
    """
    Fetch historical market data for a given coin over a number of days.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": currency, "days": days}
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
    data = response.json()
    prices = pd.DataFrame(data["prices"], columns=["timestamp", "price"])
    prices["timestamp"] = pd.to_datetime(prices["timestamp"], unit="ms")
    return prices
