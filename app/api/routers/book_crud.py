from fastapi import APIRouter, Depends
from services import books_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import Book, BookCreate, BookUpdate
from sercurity import JWTBearer,decodeJWT

router = APIRouter()


@router.get("/", tags=["book"], response_model=list[Book])
async def get_books(session: Session = Depends(create_session)):
    # return books_services.get_all_books(session,skip,limit, skip: int = 0, limit: int = 100)
    return books_services.get_all_books(session)


@router.get("/{id}", tags=["book"], response_model=Book)
async def get_book_by_id(id: int, session: Session = Depends(create_session)):
    return books_services.get_book(session, id)


@router.post("/", tags=["book"], response_model=Book)
async def create_a_book(book_schemas: BookCreate, session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["admin", "staff"]))):
    return books_services.add_book(session, book_schemas)


@router.put("/{id}", tags=["book"], response_model=Book)
async def update_a_book( id: int, book_schema: BookUpdate, session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["admin", "staff"]))):
     return books_services.modify_book(session,id,book_schema)


@router.delete("/{id}", tags=["book"], response_model=Book)
async def Delete_a_book( id: int ,session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["admin", "staff"]))):
      return books_services.remove_book(session,id)
#1