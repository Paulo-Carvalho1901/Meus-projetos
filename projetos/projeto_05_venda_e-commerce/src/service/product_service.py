import pandas as pd

from dto.product_dto import ProductDTO


class ProductService:

    def __init__(self, repository):
        self.repository = repository

    def process_products(self):

        products = self.repository.get_products()

        result = []

        for p in products:

            dto = ProductDTO(
                id=p["id"],
                title=p["title"],
                price=p["price"],
                category=p["category"],
                rating=p["rating"]["rate"]
            )

            result.append(dto.__dict__)

        df = pd.DataFrame(result)

        df = df.sort_values(
            by="price",
            ascending=False
        )

        return df