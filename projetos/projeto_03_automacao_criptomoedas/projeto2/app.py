import pandas
import requests


class CoinGeckoClient:

    BASE_URL = "https://api.coingecko.com/api/v3"

    def obter_moedas(self):
        endpooint = f"{self.BASE_URL}/coins/markets"

        params = {
            "vs_currency": "usd",
            "per_page": 50
        }

        response = requests.get(endpooint, params=params)
        response.raise_for_status()

        return response.json()
    

