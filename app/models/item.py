import imp
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    name: str
    brand: str
    type: str
    description: str
    price: Optional[float]
    model_path: str
    model_type: Optional[str]

