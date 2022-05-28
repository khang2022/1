from dbmodels import Users
from .services_base import BaseService, Session
from sercurity import get_password_hash


class UsersService(BaseService[Users]):
    def get_by_email(self, session: Session, email: str):
        return session.query(Users).filter(Users.email == email).first()
    
    
    def create_one2(self, session: Session, obj: any):
        instance = super().create_one2(session, obj)
        instance.password = get_password_hash(instance.password)
        instance = self.save(session, instance)
        return instance
    
       
users_services = UsersService(Users) 
#1