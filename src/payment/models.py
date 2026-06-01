from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func
import enum

from src.utilis.db import Base

class PaymentMethodEnum(str, enum.Enum):
    COD = "COD"
    CARD = "CARD"

class PaymentStatusEnum(str, enum.Enum):
    PENDING = "Pending"
    SUCCESS = "Success"
    FAILED = "Failed"

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer,ForeignKey("orders.id"),nullable=False)

    payment_method = Column(Enum(PaymentMethodEnum),nullable=False)

    payment_status = Column(Enum(PaymentStatusEnum),default=PaymentStatusEnum.PENDING)

    transaction_id = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True),server_default=func.now())