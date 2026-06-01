from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.payment.models import Payment
from src.payment.dtos import PaymentSchema, PaymentStatus


def add_payment(db: Session, body: PaymentSchema):

    new_payment = Payment(
        order_id=body.order_id,
        payment_method=body.payment_method,
        payment_status=body.payment_status,
        transaction_id=body.transaction_id
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)

    return {
        "message": "Payment created successfully",
        "payment_id": new_payment.id
    }
def verify_payment(db: Session, body):

    payment = db.query(Payment).filter(Payment.id == body.payment_id).first()

    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    payment.payment_status = body.status
    payment.transaction_id = body.transaction_id

    db.commit()
    db.refresh(payment)

    return {
        "message": "Payment verified successfully"
    }