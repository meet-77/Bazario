from src.products.dtos import ProductSchema
from sqlalchemy.orm  import Session
from fastapi import HTTPException , status
from src.products.models import ProductModel
from src.users.models import UserModel



def create_product(body: ProductSchema, db: Session, user: UserModel):
    if user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can create products"
        )
    data = body.model_dump()
    new_product = ProductModel(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        stock_quantity=data["stock_quantity"],
        image_url=data["image_url"],
        user_id=user.id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {
        "status": "task created successfully",
        "data": new_product
    }
    

def get_product(db:Session , user:ProductModel):
    product = db.query(ProductModel).filter(ProductModel.user_id == user.id).all()
    return product


def one_product(product_id:int , db:Session):
    one_product= db.query(ProductModel).get(product_id)
    
    if not one_product:
        return  HTTPException(status_code=404 , detail="Product id is not found that....")
    return {"status":"Task fetched success" , "data":one_product}


def update_product(product_id:int , body:ProductSchema , db:Session , user:UserModel):
    
    one_product = db.get(ProductModel , product_id)
    if not one_product:
        raise HTTPException(status_code=404, detail="Product id is not found in data")
    
    if one_product.user_id != user.id:
        raise HTTPException(status_code=404, detail="unautorized in user")
    
    one_product.name = body.name
    one_product.description = body.description
    one_product.price = body.price
    one_product.stock_quantity = body.stock_quantity
    one_product.image_url = body.image_url
    
    db.commit()
    db.refresh(one_product)
    
    return {"status": "Porudcts is updated....", "data": one_product}
    
def delete_product(product_id:int , db:Session , user:UserModel):
    
    one_product = db.get(ProductModel , product_id)
    if not one_product:
        raise HTTPException(status_code=404, detail="Product id is not found in data")
    
    if one_product.user_id != user.id:
        raise HTTPException(status_code=404, detail="unautorized in user")
    
    db.delete(one_product)
    db.commit()
    return {"status": "Product  is deleted......."}
    