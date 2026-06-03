import pandas as pd
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
    

class ProcessadorDados:

    @staticmethod
    def transformar(dados):

        return pd.DataFrame([
            {
                "nome": item["name"],
                "simbolo": item["symbol"],
                "preco": item["current_price"]
            }
            for item in dados
        ])
        
