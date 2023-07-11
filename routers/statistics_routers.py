from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas.customer_schemas import CreateCustomer
from schemas.user_schemas import UserCreate
from functions.token import get_current_user
from utils.role_aniqlovchi import role_admin
from functions.customer_functions import create_customer,every_customers,update_customer
from utils.jicha_kereli import get_with_id_anything
from models.customers import Customers
from schemas.customer_schemas import UpdateCustomer
from functions.statistics_function import all_statistics
statistic_router = APIRouter(tags=["Statistika"])

@statistic_router.get("/statistics")
def get_all_statistics(db: Session = Depends(get_db)):
    all_statistics(db)
