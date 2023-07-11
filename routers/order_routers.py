from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.order_funcs import all_orders, create_order, update_order, delete_order
from models.order import Orders
from functions.token import get_current_user
from utils.jicha_kereli import get_with_id_anything
from schemas.order_schemas import CreateOrder, UpdateOrder
from schemas.user_schemas import UserCreate
from database import get_db
from utils.role_aniqlovchi import role_admin

order_router = APIRouter(tags=["Orders"])


@order_router.get("/get_orders")
def hamma_orderlar(search: str = None, id: int = 0, page: int = 0, limit: int = 10, db: Session = Depends(get_db),
              request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Orders, id)
    return all_orders(search, page, limit, db)


@order_router.post("/take_order")
def order_ochish(yangi_order: CreateOrder, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    create_order(yangi_order, db, request_user)
    raise HTTPException(status_code=200, detail="Order ochildi")


@order_router.put("/update_order")
def orderni_yangilash(shu_orderni: UpdateOrder, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_order(shu_orderni, db, request_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


@order_router.delete("/delete_order")
def delete_order_main(id: int, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    delete_order(id, db)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")






