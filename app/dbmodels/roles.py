from sqlalchemy import  Column,Integer,String
from sqlalchemy.orm import relationship
from core.base import Base


#1
class Roles(Base):
    __tablename__ = "roles"
    id          = Column(Integer, primary_key=True)
    title       = Column(String(255))
  
    # connection
    users_list =  relationship("Users", back_populates="role") # link one to many
    
     
   