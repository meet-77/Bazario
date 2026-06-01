from sqlalchemy import Column , String , Integer , DateTime ,ForeignKey, Boolean , func , Float
from src.utilis.db import Base 
from sqlalchemy.orm import relationship

class ProductModel(Base):
    __tablename__ = "product_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)
    stock_quantity = Column(Integer, default=0)
    image_url = Column(String)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    created_at = Column(DateTime, server_default=func.now())

    # optional but recommended
    user = relationship("UserModel", backref="products")