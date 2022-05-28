from fastapi import  FastAPI, Depends , HTTPException
from services import users_services,books_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import UserCreate, LoginForm , BookCreate, Book
from sercurity import verify_password, encodeJWT ,JWTBearer


app = FastAPI()


@app.post("/signup", tags= ["user signup"]) # check unique for user
async def sign_up(newcomer: UserCreate , session: Session = Depends(create_session)):
      return users_services.create_one(session, newcomer)



@app.post("/login", tags=["user login"])
async def log_in(body : LoginForm , session: Session = Depends(create_session)):
      user =  users_services.get_by_email(session,body.email)
      if not user : 
          raise HTTPException(status_code=400, detail="Incorrect username or password")
      if not verify_password(body.password, user.password ):
          raise HTTPException(status_code=400, detail="Incorrect username or password")
      return encodeJWT(body.email)
  


@app.post("/addbook",  dependencies=[Depends(JWTBearer())],tags=["books"], response_model= Book)
async def create_a_book( book_schemas: BookCreate, session: Session = Depends(create_session)):
     return books_services.create_one2(session,book_schemas)



     



            