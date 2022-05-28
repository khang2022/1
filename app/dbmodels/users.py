from sqlalchemy import Integer, String, Column,ForeignKey
from sqlalchemy.orm import relationship
from core.base import Base



class Users(Base):
    __tablename__ = "users"
    id          = Column(Integer, primary_key=True)
    email       = Column(String(255),nullable=False, unique=True)
    password    = Column(String(255))
    first_name  = Column(String(255))
    last_name   = Column(String(255))
    tel_no      = Column(String(255))
    address     = Column(String(255))
    
    roles_id = Column(Integer, ForeignKey('roles.id')) # PK
    
   
    # connection
    customer =  relationship("Customers", back_populates="user", uselist = False) # link one to one 
    staff    =  relationship("Staffs"   , back_populates="user", uselist = False) # link one to one 
    role =  relationship("Roles", back_populates="users_list") # link many to one
    
 #1   
    # @property
    # def password(self):
    #     return self.password

    # @password.setter
    # def password(self, password):
    #     self.password = hash_password
     
   #1