from sqlalchemy import  Column, ForeignKey, Table
from core.base import Base


BookCartTable = Table(
    "book_cart",
    Base.metadata,
    Column("books_id", ForeignKey("books.id"), primary_key=True),
    Column("carts_id", ForeignKey("carts.id"), primary_key=True)    
)
#1