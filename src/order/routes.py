from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.users.models import UserModel
from src.utilis.db import get_db
from src.order import controller
from src.utilis.helpers import is_authenticated
from src.order.dtos import OrderSchema


order_routes = APIRouter(prefix="/orders")

@order_routes.post("/create")
def create_order(body: OrderSchema,db: Session = Depends(get_db),user: UserModel = Depends(is_authenticated)):
    return controller.create_order(db, user.id, body)

@order_routes.get("/details")
def get_order_details(db: Session = Depends(get_db),user: UserModel = Depends(is_authenticated)):
    return controller.get_order_details(db, user.id)

@order_routes.get("/details/{id}")
def get_order_id(
    id: int,
    db: Session = Depends(get_db),
    user: UserModel = Depends(is_authenticated)
):
    return controller.get_order_id(db, user.id, id)