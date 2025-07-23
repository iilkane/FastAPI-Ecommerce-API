from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime
from app.schemas.carts import CartBase

class BaseConfig:
    from_attributes = True


class UserBase(BaseModel):
    id : int
    username : str
    email : EmailStr
    password : str
    full_name : str
    is_active : bool
    created_at : datetime
    role : str
    carts : List[CartBase]

    class Config(BaseConfig):
        pass


class UserCreate(BaseModel):
    full_name : str
    username : str
    email : EmailStr
    password : str

    class Config(BaseConfig):
        pass

class UserUpdate(UserCreate):
    pass


class UserOut(UserBase):
    message : str
    data : UserBase

    class Config(BaseConfig):
        pass


class UserOut(UserBase):
    message : str
    data : List[UserBase]

    class Config(BaseConfig):
        pass


class UserOutDelete(UserBase):
    message : str
    data : UserBase

    class Config(BaseConfig):
        pass
