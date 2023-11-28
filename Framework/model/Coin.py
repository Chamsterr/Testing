from pydantic import BaseModel

class Coin(BaseModel):
    name: str
    quantity: int
    price: int