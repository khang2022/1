from datetime import date
from pydantic import BaseModel
from .f_category import CategoryCreate,CategoryUpdate
#1
#1
class BookBase (BaseModel):

    book_name: str | None
    author: str | None
    publication_year: date | None
    publishing_company: str | None
    price: int | None
    store_area: str | None

    class Config:
        orm_mode = True


class BookCreate (BookBase, CategoryCreate):
    pass


class BookUpdate (BookBase, CategoryUpdate):
    pass


class Book (BookBase):
    id: int
    sold: bool | None
    categorys_list: list | None
