from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from services import customers_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import CustomerInfor, SignUpBase, CustomerUpdate
from sercurity import JWTBearer,decodeJWT

#1
router = APIRouter()


@router.get("/", tags=["customer"], response_model=list[CustomerInfor])
async def find_customers(
    session: Session = Depends(create_session),
    credentials: str = Depends(
        JWTBearer(["admin", "manager", "staff"]))
):
    print(decodeJWT(credentials))
    return customers_services.get_customers(session)


@router.get("/{id}", tags=["customer"], response_model=CustomerInfor)
async def get_customer_by_id(id: int, session: Session = Depends(create_session),
                             credentials: str = Depends(
                             JWTBearer(["admin", "manager", "staff"]))):
    return customers_services.get_customer(session, id)


@router.post("/", tags=["customer"], response_model=CustomerInfor)
async def create_customer(body_form: SignUpBase, session: Session = Depends(create_session),
                          credentials: str = Depends(
                          JWTBearer(["admin", "manager", "staff"]))):
    return customers_services.add_customer(session, body_form)


@router.put("/{id}", tags=["customer"], response_model=CustomerInfor)
async def update_customer(id: int, body_form: CustomerUpdate, session: Session = Depends(create_session),
                         credentials: str = Depends(
                         JWTBearer(["admin", "manager", "staff"]))):
    return customers_services.modify_customer(session, id, body_form)


@router.delete("/{id}", tags=["customer"])
async def delete_customer(id: int, session: Session = Depends(create_session),
                         credentials: str = Depends(
                         JWTBearer(["admin", "manager", "staff"]))):
    customers_services.remove_customer(session, id)
