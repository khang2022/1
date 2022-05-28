from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.orm import relationship
from core.base import Base

class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    
 #1   
    # connection
    user =  relationship("Users", back_populates="customer") # link one to one with user 
                                                                 
   
    cart_list =  relationship("Carts", back_populates="customer") # link one to many with carts
    