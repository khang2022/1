from fastapi import  APIRouter, Depends
from services import  carts_services
from sqlalchemy.orm import Session
from core.engine import create_session
from schemas import   Cart,  CartCreate , CartUpdate
from sercurity import JWTBearer,decodeJWT   



router = APIRouter()



# /book/{id}

# /book/

# /book/{id}/abc => nh

#1

@router.get("/{id}", tags=["cart"], response_model=  Cart)
async def get_cart(id: int, session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["admin","manager","staff","customer"]))):
    return  carts_services.show_cart(session,id, credentials)


@router.post("/{id}", tags=["cart"], response_model= Cart)
async def create_cart(cart_schemas:  CartCreate , session: Session = Depends(create_session),
                        credentials: str = Depends(
                        JWTBearer(["customer"]))):
     return  carts_services.buy_book(session, cart_schemas,credentials )
 

# @router.put("/", tags=["cart"], response_model= Cart)
# async def update_a_cart( id: int, cart_schemas:  CartUpdate, session: Session = Depends(create_session)):
#      return  carts_services.update(session,id, cart_schemas)
 

# @router.delete("/{id}", tags=["cart"], response_model= Cart)
# async def delete_a_cart( id: int ,session: Session = Depends(create_session)):
#      return carts_services.delete_one(session,id)
      
      



 
 