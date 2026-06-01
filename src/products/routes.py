from fastapi import APIRouter , Depends
from src.products import controller  
from src.products.dtos import ProductSchema
from src.utilis.db import get_db
from sqlalchemy.orm import Session
from src.utilis.helpers import is_authenticated
from src.users.models import UserModel

product_routes = APIRouter(prefix="/products")

@product_routes.post("/create")
def create_product(body:ProductSchema  , db:Session = Depends(get_db) , user:UserModel = Depends(is_authenticated)):
    # print(user.id)
    return controller.create_product(body , db , user)

@product_routes.get("/get_product")
def get_product(db:Session=Depends(get_db) , user:UserModel = Depends(is_authenticated)):
    return controller.get_product(db,user)

@product_routes.get("/get_one_product/{product_id}")
def get_one_product(product_id:int , db:Session =Depends(get_db) , user:UserModel = Depends(is_authenticated)):
    return controller.one_product(product_id , db)

@product_routes.put("/update_product/{product_id}")
def update_product(product_id:int , body:ProductSchema , db:Session=Depends(get_db) , user:UserModel =Depends(is_authenticated)):
    return controller.update_product(product_id , body , db , user )


@product_routes.delete("/delete_product/{product_id}")
def delete_product(product_id:int , db:Session=Depends(get_db) , user:UserModel=Depends(is_authenticated)):
    return controller.delete_product(product_id , db , user)