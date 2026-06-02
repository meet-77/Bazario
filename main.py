from fastapi import FastAPI
from src.utilis.db import Base , engine
from src.users.routes import user_routes
from src.carts.routes import cart_routes
from src.products.routes import product_routes
from src.order.routes import order_routes
from src.payment.routes import payment_routes
Base.metadata.create_all(engine)


app = FastAPI(title="this is a Bazario online webiste ")

app.include_router(user_routes)
app.include_router(product_routes)
app.include_router(cart_routes)
app.include_router(order_routes)
app.include_router(payment_routes)


@app.get("/")
def home():
    return {"message": "FastAPI deployed on Vercel"}