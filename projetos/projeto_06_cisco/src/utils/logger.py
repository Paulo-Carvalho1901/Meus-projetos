import os
import logging


def get_logger():

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/application.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(__name__)