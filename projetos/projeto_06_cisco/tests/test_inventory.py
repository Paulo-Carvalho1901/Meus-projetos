from src.repository.cisco_repository import CiscoRepository
from src.service.inventory_service import InventoryService


def test_inventory():

    repository = CiscoRepository()

    service = InventoryService(
        repository
    )

    df = service.process()

    assert len(df) > 0