from pydantic import BaseModel


class RoleBase (BaseModel):
  
    title      : str = None
    # admin      : bool = None
    # manager    : bool = None
    # staff      : bool = None
          
    class Config:
        orm_mode = True
#1
class RoleCreate (RoleBase):
    pass

class RoleUpdate (RoleBase):
    pass


class Role (RoleBase):
    id : int
