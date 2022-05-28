from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config



SQL_URL= config("sql_url")



engine = create_engine(SQL_URL)
SessionLocal = sessionmaker(bind=engine)
#1

def create_session(): #Each time, a session is being generate, they will execute, then close..... then generate a new one -> repeat
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
