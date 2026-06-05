from src.service.product_service import ProductService

class FakeRepository:

    def get_products(self):

        return [
            {
                "id": 1,
                "title": "Notebook",
                "price": 1000,
                "category": "Tech",
                "rating": {
                    "rate": 4.5
                }
            }
        ]


def test_dataframe_not_empty():

    repo = FakeRepository()

    service = ProductService(repo)

    df = service.process_products()

    assert len(df) == 1