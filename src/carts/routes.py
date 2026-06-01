from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.users.models import UserModel
from src.utilis.db import get_db
from src.carts import controller

from src.utilis.helpers import is_authenticated
from src.carts.dtos import  CartItemSchema
cart_routes = APIRouter(prefix="/carts")


@cart_routes.post("/add")
def add_to_cart(body: CartItemSchema, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.add_to_cart(db, user.id, body.product_id, body.quantity)
   

@cart_routes.get("/details")
def cart_details(db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    return controller.get_or_create_cart(db, user.id)


@cart_routes.get("/get_cart")
def get_cart(db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    try:
        cart = controller.get_cart(db, user.id)
        if not cart:
            raise HTTPException(status_code=404, detail="Cart not found")
        return cart
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@cart_routes.delete("/remove")
def remove_from_cart(product_id: int, db: Session = Depends(get_db), user: UserModel = Depends(is_authenticated)):
    try:
        return controller.remove_from_cart(db, user.id, product_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))