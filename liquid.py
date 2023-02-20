from dataclasses import dataclass
from typing import Optional

@dataclass
class Liquid:
    flavour: str
    retail_price: int
    base_price: int
    quantity: int
    volume_ml: int
    status: int
    buying_method: str
    created: str = ""
    id: Optional[int] = None

