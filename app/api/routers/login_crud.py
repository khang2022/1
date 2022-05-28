from fastapi import  APIRouter, Depends , HTTPException
from services import users_services,roles_services,staffs_services,customers_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import  LoginForm 
from sercurity import verify_password, encodeJWT 

#1

router = APIRouter()



@router.post("/", tags=["user-login"])
async def log_in(body : LoginForm , session: Session = Depends(create_session)):
      user =  users_services.get_by_email(session,body.email)
      if not user : 
          raise HTTPException(status_code=400, detail="Incorrect username or password")
      if not verify_password(body.password, user.password ):
          raise HTTPException(status_code=400, detail="Incorrect username or password")
      
      role = roles_services.get_one(session,user.roles_id)
     
      role =role.title if role else "customer"  # c1
      # c2  role = role.title if role.title else "customer" 
      if role == "customer":
          customer = customers_services.get_customer_by_user_id(session,user.id)
          id = customer.id
      else:
          internal = staffs_services.get_staff_by_user_id(session,user.id)
          id = internal.id   
          
      return encodeJWT(body.email,role,id)
  