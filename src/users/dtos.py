from pydantic import BaseModel , EmailStr 
from typing import Optional

class UserSchma(BaseModel):
    
    username:str
    password: str
    email : EmailStr
    phone_number:int
    admin_key: Optional[str] = None
    
class UserResponceSchma(BaseModel):
    id:int
    username: str
    email : EmailStr
    phone_number:int
    
    class Config:
        from_attributes = True 
        
class LoginSchema(BaseModel):
    email: EmailStr
    password: str