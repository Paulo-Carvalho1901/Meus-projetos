from dataclasses import dataclass


@dataclass
class ProductDTO:
    id: int
    title: str
    price: float
    category: str
    reting: float
