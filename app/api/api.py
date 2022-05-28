from fastapi import APIRouter
from .routers import book_crud,cart_crud, role_crud,staff_crud,customer_crud,login_crud

api_router = APIRouter()

api_router.include_router(login_crud.router, prefix="/user-login", tags=["user-login"])
api_router.include_router(staff_crud.router, prefix="/staff", tags=["staff"])
api_router.include_router(customer_crud.router, prefix="/customer", tags=["customer"])
api_router.include_router(cart_crud.router, prefix="/cart", tags=["cart"])
api_router.include_router(book_crud.router, prefix="/book", tags=["book"])
#1



