from fastapi import  APIRouter, Depends
from services import  roles_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import   Role,  RoleCreate , RoleUpdate 


router = APIRouter()


@router.get("/", tags=["role"], response_model=list[Role])
async def find_roles(session: Session = Depends(create_session) , skip: int = 0, limit: int = 100):
    return  roles_services.get_all(session,skip,limit)


@router.get("/{id}", tags=["role"], response_model= Role)
async def get_role_by_id(id: int, session: Session = Depends(create_session)):
    return  roles_services.get_one(session,id)


@router.post("/", tags=["role"], response_model= Role)
async def create_role(role_schemas:  RoleCreate = Depends(RoleCreate), session: Session = Depends(create_session)):
     return  roles_services.create_one(session, role_schemas)
 
#1
@router.put("/{id}", tags=["role"], response_model= Role)
async def update_role( id: int, role_schemas:  RoleUpdate= Depends( RoleUpdate), session: Session = Depends(create_session)):
     return  roles_services.update(session,id, role_schemas)
 

@router.delete("/{id}", tags=["role"], response_model= Role)
async def delete_role( id: int ,session: Session = Depends(create_session)):
       roles_services.delete_one(session,id)
       session.close()
      



 
 