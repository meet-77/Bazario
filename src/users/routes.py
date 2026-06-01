from fastapi import APIRouter , Depends , status , Request
from sqlalchemy.orm import Session
from src.users.dtos import UserSchma , UserResponceSchma , LoginSchema
from src.utilis.db import get_db
from src.users import controller



user_routes = APIRouter(prefix="/user")

@user_routes.post("/register" ,response_model=UserResponceSchma, status_code=status.HTTP_201_CREATED)
def register(body:UserSchma ,db: Session = Depends(get_db)):
    return controller.register(body , db)

@user_routes.post("/login" , status_code=status.HTTP_200_OK)
def login(body:LoginSchema , db:Session=Depends(get_db)):
    return controller.login_user(body , db)


@user_routes.get("/is_auth" , status_code=status.HTTP_200_OK , response_model=UserResponceSchma) 
def is_auth(request : Request , db: Session = Depends(get_db)):
    return controller.is_authenticated(request ,db)

