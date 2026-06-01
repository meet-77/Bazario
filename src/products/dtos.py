from pydantic import BaseModel 
from typing import Optional

class ProductSchema(BaseModel):
    
    name:str
    description:str
    image_url:str
    price:float
    stock_quantity:int


class ProductResponceSchema(BaseModel):
    
    id:int
    name:str
    price:float
    stock_quantity:int
    
    class Config:
        from_attributes = True 