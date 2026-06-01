from pydantic import BaseModel
from datetime import datetime
from typing import List


class CartItemSchema(BaseModel):
    id: int | None = None
    cart_id:int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True


class CartSchema(BaseModel):
    id: int | None = None
    user_id: int
    created_at: datetime | None = None
    items: List[CartItemSchema] = []

    class Config:
        orm_mode = True