from fastapi import HTTPException
from dbmodels import Books, Categorys
from .services_base import BaseService, Session
from schemas import BookCreate, BookUpdate
from fastapi.encoders import jsonable_encoder

#1
class BooksService(BaseService[Books]):
    def get_by_name(session: Session, name: str):
        return session.query(Books).filter(Books.name == name).first()

    def get_all_books(self, session: Session):  # Get all data from a table
        result = session.query(Books).all()
        return result

    def get_book(self, session: Session, id: int):
        result = session.query(Books).filter(Books.id == id).first()
        return result
    

    def add_book(self, session: Session, body_form: BookCreate):

        book_form = Books(
            store_area=body_form.store_area,
            book_name=body_form.book_name,
            author=body_form.author,
            publication_year=body_form.publication_year,
            publishing_company=body_form.publishing_company,
            sold=False,  # constanly add book
            price=body_form.price
        )

        # print(jsonable_encoder(body_form.title))
        for title in body_form.title:
            #  print(title.value)
            catergory = Categorys(title=title.value)
            book_form.categorys_list.append(catergory)

        # print(book_from.__dict__)
        session.add(book_form)
        session.commit()
        session.refresh(book_form)  # read again from db
        return book_form

    def modify_book(self, session: Session, id: int, body_form: BookUpdate):
        available: Books = session.query(Books).filter(Books.id == id).first()
        if not available:
            raise HTTPException(
                status_code=404,  detail="Not found !")

        available.store_area = body_form.store_area,
        available.book_name = body_form.book_name,
        available.author = body_form.author,
        available.publication_year = body_form.publication_year,
        available.publishing_company = body_form.publishing_company,
        available.price = body_form.price

        # print(jsonable_encoder(body_form.title))
        # title_list = body_form.title
        
        # titles = session.query(Categorys).filter(Categorys.id.in_ == title_list).all()
        # available.categorys_list = titles

        # print(book_from.__dict__)
        session.commit() # khi update chỉ việc commit bởi trong session đã có rồi 
        session.refresh(available)  # read again from db
        return available

    def remove_book(self, session: Session, id: int):
        available = session.query(Books).filter(Books.id == id).first()
        if not available:
            raise HTTPException(
                status_code=404,  detail="This book is not exist !")
        self.delete_one(session, id)

    
books_services = BooksService(Books)
