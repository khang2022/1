from fastapi import  APIRouter, Depends 
from services import  staffs_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import  SignUp , StaffInfo,\
     StaffUpdate,StaffUpdate
from sercurity import JWTBearer,decodeJWT     
     


router = APIRouter()


@router.get("/", tags=["staff"],response_model = list[StaffInfo])
async def find_staffs(session: Session = Depends(create_session)
                    #   ,credentials: str = Depends(
                    #  JWTBearer(["admin", "manager", "staff"]))
                    ):
     return staffs_services.get_staffs(session)
     


@router.get("/{id}", tags=["staff"] , response_model = StaffInfo)
async def get_staff_by_id(id: int, session: Session = Depends(create_session),
                         credentials: str = Depends(
                         JWTBearer(["admin", "manager", "staff"]))):
     return staffs_services.get_staff(session, id)



@router.post("/", tags=["staff"], response_model = StaffInfo)
async def create_staff(body_form : SignUp  , session: Session = Depends(create_session),
                      credentials: str = Depends(
                      JWTBearer(["admin", "manager", "staff"]))):
     return staffs_services.add_staff(session, body_form )  
    
    
#1   
@router.put("/{id}", tags=["staff"] , response_model = StaffInfo)
async def update_staff(id : int ,body_form : StaffUpdate  , session: Session = Depends(create_session),
                       credentials: str = Depends(
                       JWTBearer(["admin", "manager", "staff"]))):
    return staffs_services.modify_staff(session,id ,body_form )
     
 
 
@router.delete("/{id}", tags=["staff"] , response_model = int)
async def delete_staff( id: int ,session: Session = Depends(create_session),
                       credentials: str = Depends(
                       JWTBearer(["admin", "manager", "staff"]))):
     return staffs_services.delete_staff (id ,session)



 
 