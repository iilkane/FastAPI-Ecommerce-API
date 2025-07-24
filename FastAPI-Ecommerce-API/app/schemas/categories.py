from pydantic import BaseModel, Field
from typing import List

class BaseConfig:
    from_attributes = True


class CategoryBase(BaseModel):
    id : int 
    name : str

    class Config(BaseConfig):
        pass


class CategoryCreate(BaseModel):
    name : str

    class Config(BaseConfig):
        pass


class CategoryUpdate(BaseModel):
    name : str

    class Config(BaseConfig):
        pass


class CategoryDelete(BaseModel):
    id : int
    name : str

    class Config(BaseConfig):
        pass 


class CategoryOut(BaseModel):
    message : str
    data : CategoryBase

    class Config(BaseConfig):
        pass


class CategoriesOut(BaseModel):
    message : str
    data : List[CategoryBase]
    
    class Config(BaseConfig):
        pass 


class CategoryDeleteOut(BaseModel):
    message: str
    data : CategoryDelete

    class Config(BaseConfig):
        pass 

