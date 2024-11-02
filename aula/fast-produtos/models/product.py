from pydantic import BaseModel

class Product(BaseModel):
    """
    id, name, description, price, in_stock
    """
    id: int
    name: str
    description: str
    price: float
    in_stock: bool
