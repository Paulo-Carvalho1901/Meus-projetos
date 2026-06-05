import requests


class ProductRepository:

    def __init__(self, api_url):
        self.api_url = api_url

    def get_products(self):

        response = requests.get(
            self.api_url,
            timeout=30
        )

        response.raise_for_status()

        return response.json()