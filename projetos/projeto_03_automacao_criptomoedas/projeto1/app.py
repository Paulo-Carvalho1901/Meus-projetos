# importes necessarios
import requests
import pandas as pd
from datetime import datetime

def busca_dados():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "par_page": 20,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params, timeout=30)

    response.raise_for_status()

    return response.json()

