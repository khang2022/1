from core.engine import engine
import dbmodels




dbmodels.Base.metadata.create_all(engine)
print("Successfully create database")
#Create database using SQLAlchemy models
