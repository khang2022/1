from fastapi import  FastAPI, Depends
from services import Books_services
from sqlalchemy.orm import Session
from core.engine import create_session





app = FastAPI()

@app.get("/book/{id}")
async def read_books(id: int, session: Session = Depends(create_session)):
      return Books_services.get_one(session, id)


