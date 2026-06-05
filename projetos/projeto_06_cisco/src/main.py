import os

from repository.cisco_repository import CiscoRepository
from service.inventory_service import InventoryService
from report_generator import generate_html

from utils.logger import get_logger

logger = get_logger()

os.makedirs("output", exist_ok=True)
os.makedirs("reports", exist_ok=True)


def main():

    try:

        repository = CiscoRepository()

        service = InventoryService(
            repository
        )

        df = service.process()

        df.to_csv(
            "output/inventory.csv",
            sep=";",
            index=False
        )

        generate_html(df)

        logger.info(
            "Inventário gerado com sucesso"
        )

        print(df)

    except Exception as error:

        logger.error(error)

        raise


if __name__ == "__main__":
    main()