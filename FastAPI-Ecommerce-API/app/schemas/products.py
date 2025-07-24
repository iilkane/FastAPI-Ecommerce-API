from pydantic import BaseModel,validator
from typing import List,Optional,ClassVar
from datetime import datetime
from app.schemas.categories import CategoryBase

class BaseConfig:
    from_attributes = True


class ProductBase(BaseModel):
    id : int
    title : str
    description : Optional[str]
    price : int

    @validator("discount_percentage", pre=True)
    def validate_discount_percentage(cls,v):
        if v<0 or v>100:
            raise ValueError("False")
        return v
    
    discount_percentage : float
    rating : float
    stock : int
    images : List[str]
    is_published : bool
    created_at : datetime
    category_id :int
    category : CategoryBase

    class Config(BaseConfig):
        pass


class ProductCreate(ProductBase):
    id : ClassVar[int]
    category: ClassVar[CategoryBase]

    class Config(BaseConfig):
        pass

class ProductUpdate(ProductBase):
    pass


class ProductOut(ProductBase):
    message : str
    data : ProductBase

    class Config(BaseConfig):
        pass

class ProductOut(ProductBase):
    message : str
    data : List[ProductBase]

    class Config(BaseConfig):
        pass


class ProductDelete(ProductBase):
    category: ClassVar[CategoryBase]


class ProductOutDelete(BaseModel):
    message: str
    data: ProductDelete