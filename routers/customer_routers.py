from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas.customer_schemas import CreateCustomer
from schemas.user_schemas import UserCreate
from functions.token import get_current_user
from utils.role_aniqlovchi import role_admin
from functions.customer_functions import create_customer, every_customers, update_customer
from utils.jicha_kereli import get_with_id_anything
from models.customers import Customers
from schemas.customer_schemas import UpdateCustomer
customer_router = APIRouter(tags=["Customers"])


@customer_router.get("/get_customers")
def get_all(search: str = None,
            id: int = 0,
            page: int = 0,
            limit: int = 10,
            db: Session = Depends(get_db),
            current_user: UserCreate = Depends(get_current_user)):
    role_admin(current_user)
    if page < 0 or limit < 0:
        raise HTTPException(
            status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Customers, id)
    return every_customers(search, page, limit, db)


@customer_router.post("/create_market")
def create_new_customer(new_customer: CreateCustomer,
                        db: Session = Depends(get_db),
                        current_user: UserCreate = Depends(get_current_user)):
    role_admin(current_user)
    create_customer(new_customer, db, current_user)
    raise HTTPException(status_code=200, detail="Yangi customer qoshildi")


@customer_router.put("/update_customer")
def main_update_customer(for_update: UpdateCustomer,
                         db: Session = Depends(get_db),
                         current_user: UserCreate = Depends(get_current_user)
                         ):

    role_admin(current_user)
    update_customer(for_update, db, current_user)
