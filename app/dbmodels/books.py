from sqlalchemy import Integer, String, Column,DateTime,Boolean,BigInteger
from sqlalchemy.orm import relationship
from core.base import Base
from .book_cart import BookCartTable

#1
class Books(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    store_area  = Column(String(255))
    book_name   = Column(String(255))
    author      = Column(String(255))
    publication_year = Column(DateTime)
    publishing_company = Column(String(255))
    sold     = Column(Boolean()) 
    price = Column(BigInteger)
    
    
    # connection
    carts_list = relationship(
        "Carts",
        secondary = BookCartTable,
        back_populates = "books_list")
    
     
    categorys_list = relationship("Categorys", back_populates="book",cascade="all, delete") 
    
    
    

     




  
    