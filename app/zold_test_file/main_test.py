from fastapi import Depends, FastAPI
import dbmodels,schemas
from core.engine import SessionLocal , engine
from sqlalchemy.orm import Session


dbmodels.Base.metadata.create_all(bind = engine)

app = FastAPI()

def create_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.post("/add_book")
async def create_book(book: schemas.BookBase = Depends(schemas.BookBase), session: Session = Depends(create_database)):
    db_createbook = dbmodels.Books(
                                   store_area  = book.store_area,
                                   book_name   = book.book_name,
                                   author      = book.author,
                                   publication_year = book.publication_year, 
                                   publishing_company = book.publishing_company,
                                   price = book.price)
    # db_createbook = models.Books.create(book)
    session.add(db_createbook)
    session.commit()
    session.refresh(db_createbook)
    return db_createbook  
         
@app.get("/book/{id}")
async def read_books(id: int):
    session = Session(bind=engine)
    # readbook = session.query(dbmodels.Books).get(id)
    # session.close()
    return session.query(dbmodels.Books).filter(dbmodels.Books.id == id).first()
    # return readbook


