from turtle import title
from sqlalchemy import Integer, Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship
from core.base import Base
#1

class Categorys(Base):
    __tablename__ = "categorys"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))

    # connection
    books_id = Column(Integer, ForeignKey('books.id')
                      )  # tạo ForeignKey tới books

    book = relationship("Books", back_populates="categorys_list")
