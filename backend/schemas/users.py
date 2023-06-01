## schemas/users.py
from typing import Optional
from pydantic import BaseModel, EmailStr

## properties required during user creation
class CreateUser(BaseModel):
    username : str 
    email : EmailStr 
    password : str

class ShowUser(BaseModel):
    username : str 
    email : EmailStr 
    is_active : bool 

    class Config():
        orm_mode = True 