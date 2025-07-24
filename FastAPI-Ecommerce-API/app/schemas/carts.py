from pydantic import BaseModel, Field
from typing import List
from datetime import datetime 
from app.schemas.products import ProductBase,CategoryBase

class BaseConfig:
    from_attributes = True


class ProductBaseCart(BaseModel):
    category: CategoryBase = Field(exclude=True)

    class Config(BaseConfig):
        pass


class CartItemBase(BaseModel):
    id : int
    quantity : int
    subtotal : float
    product_id: int
    product : ProductBaseCart


class CartBase(BaseModel):
    id : int
    user_id : int
    created_at : datetime
    total_amount: float
    cart_items : List[CartItemBase]

    class Config(BaseConfig):
        pass


class CartItemCreate(BaseModel):
    product_id : int
    quantity : int 


class CartCreate(BaseModel):
    cart_items: List[CartItemCreate]


class CartUpdate(CartCreate):
    pass


class CartOutBase(BaseModel):
    id : int
    user_id : int
    created_at : datetime
    total_amount: float
    cart_items : List[CartItemBase]

    class Config(BaseConfig):
        pass


class CartOut(BaseModel):
    message : str
    data: CartBase
    
    class Config(BaseConfig):
        pass


class CartOutList(BaseModel):
    message : str
    data : List[CartBase]


class CartUserOutList(BaseModel):
    message : str
    data : List[CartBase]

    class Config(BaseConfig):
        pass 


class CartOutDelete(BaseModel):
    message: str
    data: CartOutBase

