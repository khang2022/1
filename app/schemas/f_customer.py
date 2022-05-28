from pydantic import BaseModel

#1
class CustomerBase (BaseModel):
  
    users_id    : int  = None
          
    class Config:
        orm_mode = True

class CustomerCreate (CustomerBase):
    pass

class CustomerUpdate (CustomerBase):
    pass



class Customer (CustomerBase):
    id : int



    
    
    