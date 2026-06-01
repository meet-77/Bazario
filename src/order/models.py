from sqlalchemy import Column , String , Integer,Numeric , DateTime ,ForeignKey, Boolean , func , Float 
from src.utilis.db import Base 
from sqlalchemy.orm import relationship
 
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    total_amount = Column(Numeric(10, 2), nullable=False)

    status = Column(String,default="Pending")

    payment_id = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)

    order_id = Column(Integer,ForeignKey("orders.id"),nullable=False)

    product_id = Column(Integer, ForeignKey("product_table.id"), nullable=False)

    quantity = Column(Integer, nullable=False)

    price = Column(Numeric(10, 2), nullable=False)
    order = relationship(
        "Order",
        back_populates="items"
    )