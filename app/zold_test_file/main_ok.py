from fastapi import FastAPI, Depends , HTTPException
import uvicorn
from api import api_router 
from sqlalchemy.orm import Session
from services import users_services,books_services
from sercurity import verify_password, encodeJWT ,JWTBearer
from schemas import UserCreate, LoginForm , BookCreate, Book
from core.engine import create_session




app = FastAPI()


@app.post("/login", tags=["login"])
async def log_in(body : LoginForm , session: Session = Depends(create_session)):
      user =  users_services.get_by_email(session,body.email)
      if not user : 
          raise HTTPException(status_code=400, detail="Incorrect username or password")
      if not verify_password(body.password, user.password ):
          raise HTTPException(status_code=400, detail="Incorrect username or password")
      return encodeJWT(body.email)






app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
