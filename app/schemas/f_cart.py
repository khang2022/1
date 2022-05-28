from pydantic import BaseModel
from datetime import datetime

#1
class CartBase (BaseModel):
   
    purchase_date  : datetime | None
    # quantity      : int  = None
    paymented         : bool = None
    # customer_id    : int  = None
    
         
    class Config:
        orm_mode = True

class CartCreate (CartBase):
    books_list :  list[int] | None

class CartUpdate (CartBase):
    pass


class Cart (CartBase):
    books_list : list
    id : int


  
    