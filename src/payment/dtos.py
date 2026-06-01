from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import enum

class PaymentMethod(str, enum.Enum):
    COD = "COD"
    CARD = "CARD"


class PaymentStatus(str, enum.Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"

class PaymentSchema(BaseModel):
    order_id: int
    payment_method: PaymentMethod
    transaction_id: Optional[str] = None
    payment_status: Optional[PaymentStatus] = PaymentStatus.PENDING


class PaymentResponseSchema(BaseModel):
    id: int
    order_id: int
    payment_method: PaymentMethod
    payment_status: PaymentStatus
    transaction_id: Optional[str] = None
    created_at: datetime

    class Config:
        orm_mode = True
        
class PaymentVerifySchema(BaseModel):
    payment_id: int
    status: str
    transaction_id: str