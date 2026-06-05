import os

from dotenv import load_dotenv

from repository.product_repository import ProductRepository
from service.product_service import ProductService
from utils.logger import get_logger

load_dotenv()

logger = get_logger()


def main():

    try:

        api_url = os.getenv("API_URL")

        repository = ProductRepository(api_url)

        service = ProductService(repository)

        df = service.process_products()

        output_file = "output/products.csv"

        df.to_csv(
            output_file,
            index=False,
            sep=";"
        )

        logger.info(
            "CSV gerado com sucesso"
        )

        print(df.head())

    except Exception as e:

        logger.error(str(e))

        raise


if __name__ == "__main__":
    main()