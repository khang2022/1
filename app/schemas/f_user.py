from pydantic import BaseModel
from datetime import date

#1
class UserBase (BaseModel):
  
    email       : str  = None
    password    : str  = None
    first_name  : str  = None
    last_name   : str  = None
    tel_no      : str  = None
    address     : str  = None
    roles_id    : int| None = None
         
    class Config:
        orm_mode = True

class UserCreate (UserBase):
    pass

class UserUpdate (UserBase):
    pass


class User (UserBase):
    id : str


  
    