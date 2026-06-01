
from sqlalchemy.orm  import Session
from fastapi import HTTPException , status
from src.carts.models import Cart , CartItem
from src.carts.dtos import CartSchema , CartItemSchema
from src.users.models import UserModel
from src.products.models import ProductModel

def get_or_create_cart(db: Session, user_id: int):
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not found"
        )

    cart = db.query(Cart).filter(Cart.user_id == user_id).first()

    if not cart:
        cart = Cart(user_id=user_id)
        db.add(cart)
        db.commit()
        db.refresh(cart)

    return cart


def add_to_cart(db: Session, user_id: int, product_id: int, quantity: int):
   
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise ValueError("Product not found")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if product.stock_quantity < quantity:
        raise ValueError("Not enough stock available")

    cart = get_or_create_cart(db, user_id)

    item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id,
            CartItem.product_id == product_id
        )
        .first()
    )

    if item:
        if product.stock_quantity < (item.quantity + quantity):
            raise ValueError("Exceeds available stock")

        item.quantity += quantity
    else:
        item = CartItem(
            cart_id=cart.id,
            product_id=product_id,
            quantity=quantity,
        )
        db.add(item)

    db.commit()
    db.refresh(cart)
    return cart


def get_cart(db: Session, user_id: int):
    cart = get_or_create_cart(db, user_id)

    items = (
        db.query(CartItem, ProductModel)
        .join(ProductModel, CartItem.product_id == ProductModel.id)
        .filter(CartItem.cart_id == cart.id)
        .all()
    )

    return {
        "cart_id": cart.id,
        "user_id": cart.user_id,
        "items": [
            {
                "product_id": product.id,
                "product_name": product.name,
                "price": product.price,
                "quantity": item.quantity
            }
            for item, product in items
        ]
    }


def remove_from_cart(db: Session, user_id: int, product_id: int):
    cart = get_or_create_cart(db, user_id)

    item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id,
            CartItem.product_id == product_id
        )
        .first()
    )

    if not item:
        raise ValueError("Item not found in cart")

    db.delete(item)
    db.commit()

    return cart