from sqlalchemy import Column , String , Integer , DateTime ,ForeignKey, Boolean , func , Float 
from src.utilis.db import Base 
from sqlalchemy.orm import relationship
 
class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationship
    items = relationship("CartItem", back_populates="cart", cascade="all, delete")


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True, index=True)
    cart_id = Column(Integer, ForeignKey("carts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product_table.id"), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    # Relationship
    cart = relationship("Cart", back_populates="items")