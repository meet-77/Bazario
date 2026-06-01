from src.users.dtos import UserSchma , LoginSchema
from sqlalchemy.orm import Session
from src.users.models import UserModel 
from fastapi import HTTPException
from pwdlib import PasswordHash
import jwt
from src.utilis.settings import settings
from datetime import datetime , timedelta
from fastapi import Request
from jwt.exceptions import InvalidTokenError

password_hash = PasswordHash.recommended()

def get_password_hash(password):
    return password_hash.hash(password)
    
def verify_password(plain_password , hashed_password):
    return password_hash.verify(plain_password , hashed_password) 


def register(body: UserSchma, db: Session):
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    role = "user"
    if body.email == "Admin123@gmail.com" and body.password == "admin123":
        role = "admin"
    hashed_password = get_password_hash(body.password)
    new_user = UserModel(
        username=body.username,
        email=body.email,
        phone_number=body.phone_number,
        hash_password=hashed_password,
        role=role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(body:LoginSchema , db:Session):
    user = db.query(UserModel).filter(UserModel.email==body.email).first()
    
    if not user:
        raise HTTPException(400 , detail="email is already use it....")
    
    if not verify_password(body.password , user.hash_password):
        raise HTTPException(401 , detail="password not match")  
    
    exp_time = datetime.now() + timedelta(seconds=100)
    # exp_time = datetime.now() + timedelta(minutes=settings.EXP_TIME)
    print(exp_time)
    token = jwt.encode({"_id": user.id , "exp":exp_time.timestamp()}, settings.SECRET_KEY, settings.ALGORITHM)
        
    print(exp_time)
    return {"token": token}
    
    
def is_authenticated(request:Request  ,db:Session):
    try:
        token = request.headers.get("authorization")
        if not token:
            raise HTTPException(401 , detail="you are unauthorized")
        
        token = token.split(" ")[-1]
        data = jwt.decode(token , settings.SECRET_KEY , settings.ALGORITHM )
        
        user_id = data.get("_id")
        # exp_time = int(data.get("exp"))
        
        # current_time = datetime.now().timestamp()
        # print(exp_time-current_time)
        # if current_time > exp_time:
        #     raise HTTPException(401 , detail="you are Time unauthorized")
        user = db.query(UserModel).filter(UserModel.id  == user_id).first()
        if not user:
            raise HTTPException(401 , detail="you are User unauthorized")
        # print(data)
        return user
    
    except InvalidTokenError:
         raise HTTPException(401 , detail="you are  unauthorized")