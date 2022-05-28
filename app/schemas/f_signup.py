from pydantic import BaseModel,Field,ValidationError
from enum import Enum, IntEnum



class RoleContant(str, Enum):
   admin = "admin",
   manager = "manager",
   staff = "staff"

#1
class SignUpBase(BaseModel):
    email       : str  = None
    password    : str  = None
    first_name  : str  = None
    last_name   : str  = None
    tel_no      : str  = None
    address     : str  = None


class SignUp(SignUpBase):
    
      role : RoleContant = RoleContant.staff

class StaffUpdate(SignUp):
    pass
class StaffInfo(SignUpBase):
    role       : str  = None
    staff_id   : int  = None
          
          
class CustomerInfor(SignUpBase):
    customer_id : int = None

class CustomerUpdate(SignUpBase):
    pass    