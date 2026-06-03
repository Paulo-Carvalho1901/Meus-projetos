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


def tratar_dados(dados):
    registros = []

    for moeda in dados:
        registros.append({
            "id": moeda["id"],
            "nome": moeda["name"],
            "simbolo": moeda["symbol"].upper(),
            "preco_usd": moeda["current_price"],
            "market_cap": moeda["market_cap"],
            "volume_24h": moeda["total_volume"],
            "variacao_24h": moeda["price_change_percentage_24h"],
            "ultima_    atualizacao": moeda["last_updated"]
        })


    return pd.DataFrame(registros)


def salvar_csv(df):
    data_execucao = datetime.now().strftime("%Y%m%d_%H%M%S")

    arquivo = f"moedas_{data_execucao}.csv"

    df.to_csv(
        arquivo,
        index=False,
        sep=',',
        encoding="utf-8-sig"
    )

    print(f'Arquivo salvo {arquivo}')


def main():
    try:
        dados = busca_dados()

        df = tratar_dados(dados)

        salvar_csv(df)

        print(df.head())

    except Exception as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
