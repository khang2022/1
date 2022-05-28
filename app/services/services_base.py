from typing import TypeVar, Generic
from sqlalchemy.orm import Session

from core.base import Base

ModelType = TypeVar("ModelType", bound=Base)

# This is a logic you can use to any services
class BaseService(Generic[ModelType]):  # get all "any" record from database

    def __init__(self, model):
        self.model = model

    def get_all(self, session: Session, skip: int = 0, limit: int = 100): #Get all data from a table
        # return session.query(self.model).offset(skip).limit(limit).all()
        query = session.query(self.model).offset(skip).limit(limit).all()
        return query
        

    def get_one(self, session: Session, id: int):   #Get one row with ID
        return session.query(self.model).filter(self.model.id == id).first()

    
    def create_one2(self, session: Session, obj: any): # just add to session 
        translate = self.model()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))        
        session.add(translate)
        # session.commit()
        # session.refresh(translate)
        return translate
    
    def save(self, session: Session, obj: ModelType):
        session.commit()
        session.refresh(obj)
        return obj
    
      
    def create_one(self, session: Session, obj: any):
        translate = self.model()
        for k in dict(obj):
            setattr(translate, k, getattr(obj, k, ""))
        session.add(translate)  
        session.commit()
        session.refresh(translate)
        return translate

    
    ##################3
    # def create_one_2(self, session: Session, obj: any, autoflush=True):
    #     translate = self.model()
    #     for k in dict(obj):
    #         setattr(translate, k, getattr(obj, k, ""))
    #     session.add(translate)
    #     if autoflush:
    #         session.commit()
    #         session.refresh(translate)
    #     return translate

#1
    def update(self, session: Session, id: int, data: any):
        instance = session.query(self.model).filter(self.model.id == id).first()

        if instance:
            for k in dict(data):
                setattr(instance, k, getattr(data, k, ""))
            session.add(instance)
            session.commit()
            session.refresh(instance)
        return instance



    def delete_one(self, session: Session, id: int): #Delete one row using ID
            db_delete = session.query(self.model).filter(self.model.id == id).first()
            session.delete(db_delete)
            session.commit()
            # return db_delete 
    
