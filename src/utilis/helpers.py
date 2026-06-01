from fastapi import Request , HTTPException  , Depends
from src.utilis.settings import settings
from sqlalchemy.orm import Session  
import jwt
from jwt.exceptions import InvalidTokenError
from src.users.models import UserModel
from src.utilis.db import get_db

def is_authenticated(request: Request, db: Session = Depends(get_db)):
    try:
        auth_header = request.headers.get("authorization")

        if not auth_header:
            raise HTTPException(status_code=401, detail="Unauthorized")

        token = auth_header.split(" ")[-1]

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        # print("DECODED PAYLOAD:", payload)

        user_id = payload.get("_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        
        user_id = int(user_id)

        user = db.query(UserModel).filter(UserModel.id == user_id).first()

        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return user

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")