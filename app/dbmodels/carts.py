from sqlalchemy import Integer, String, Column,Boolean, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from core.base import Base
from .book_cart import BookCartTable

#1
class Carts(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True)
    purchase_date  = Column(DateTime)
    paymented      = Column(Boolean())
    customer_id = Column(Integer, ForeignKey('customers.id'))  # PK
    
    # connection
    books_list = relationship(
        "Books",
        secondary = BookCartTable,
        back_populates = "carts_list")
    
    
    customer =  relationship("Customers", back_populates="cart_list")  # link many to one cart to customer
    
    
    
    
    

