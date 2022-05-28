from pydantic import BaseModel
from enum import Enum


#1
class CategoryContant(str,Enum):
    autobiography = 'autobiography',
    biography     = 'biography',
    economics     = 'economics',
    hobbies       = 'hobbies ',
    cookbook      = 'cookbook',
    diary         = 'diary',
    dictionary    = 'dictionary',
    encyclopedia  = 'encyclopedia',
    guide         = 'guide',
    fitness       = 'fitness',
    history       = 'history',
    architecture  = 'architecture'

class CategoryBase (BaseModel):

    title: list[CategoryContant]
    
    class Config:
        orm_mode = True

class CategoryCreate (CategoryBase):
    pass

class CategoryUpdate (CategoryBase):
    pass


class Category (CategoryBase):
    id : int