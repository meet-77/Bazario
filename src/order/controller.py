
from sqlalchemy.orm  import Session
from fastapi import HTTPException , status
from src.carts.models import Cart , CartItem
from src.carts.dtos import CartSchema , CartItemSchema
from src.users.models import UserModel
from src.products.models import ProductModel
from src.order.models import Order , OrderItem
from src.order.dtos import OrderSchema , OrderItemSchema


def create_order(db: Session, user_id: int, body: OrderSchema):

    new_order = Order(
        user_id=user_id,
        total_amount=body.total_amount,
        status=body.status,
        payment_id=body.payment_id
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for item in body.items:
        order_item = OrderItem(
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(order_item)

    db.commit()

    return {
        "message": "Order created successfully",
        "order_id": new_order.id
    }

def get_order_details(db: Session, user_id: int):

    orders = db.query(Order).filter(Order.user_id == user_id).all()
    return orders

def get_order_id(db: Session, user_id: int, order_id: int):

    order = db.query(Order).filter(
        Order.id == order_id,
        Order.user_id == user_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order