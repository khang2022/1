from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from core.base import Base
#1
class Staffs(Base):
    __tablename__ = "staffs"
    id = Column(Integer, primary_key=True, index=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    
    
    # connection
    user =  relationship("Users", back_populates="staff") # link one to one with user 
                                                                 
   
   
    