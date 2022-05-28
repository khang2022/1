from fastapi import  FastAPI, Depends
from services import Books_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import  BookCreate



app = FastAPI()

@app.get("/book/{id}")
async def get_book(id: int, session: Session = Depends(create_session)):
    return Books_services.get_one(session,id)


@app.get("/All_book/")
async def Find_list_book(session: Session = Depends(create_session) , skip: int = 0, limit: int = 100):
    return Books_services.get_all(session,skip,limit)


@app.post("/Create a book/{id}")
async def Create_a_book( Book_schemas: BookCreate = Depends(BookCreate), session: Session = Depends(create_session)):
     return Books_services.create_one(session,Book_schemas)
 

@app.put("/Update a book/{id}")
async def Update_a_book( id: int,Book_schemas: BookCreate = Depends(BookCreate), session: Session = Depends(create_session)):
     return Books_services.update(session,id,Book_schemas)
 

@app.delete("/Delete a book/{id}")
async def Delete_a_book( id: int ,session: Session = Depends(create_session)):
      Books_services.delete_one(session,id)
      session.close()
      



 
 