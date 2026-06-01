from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class OrderItemSchema(BaseModel):
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True

class OrderSchema(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int] = None
    total_amount: float
    status: Optional[str] = "Pending"
    payment_id: Optional[str] = None
    created_at: Optional[datetime] = None
    items: List[OrderItemSchema] = []

    class Config:
        orm_mode = True
        