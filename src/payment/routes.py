from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.utilis.db import get_db
from src.payment import controller
from src.payment.dtos import PaymentSchema, PaymentStatus , PaymentVerifySchema


payment_routes = APIRouter(prefix="/payment")


@payment_routes.post("/create")
def add_payment(
    body: PaymentSchema,
    db: Session = Depends(get_db)
):
    return controller.add_payment(db, body)


@payment_routes.post("/verify")
def verify_payment(
    body: PaymentVerifySchema,
    db: Session = Depends(get_db)
):
    return controller.verify_payment(db, body)