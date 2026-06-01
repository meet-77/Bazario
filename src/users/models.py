from sqlalchemy import Column, String, Integer, DateTime, func
from src.utilis.db import Base

class UserModel(Base):

    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    phone_number = Column(String, nullable=True) 

    hash_password = Column(String, nullable=False)

    created_at = Column(DateTime, server_default=func.now())

    role = Column(String, default="user") 