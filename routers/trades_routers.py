from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.order_funcs import update_order
from functions.token import get_current_user
from functions.trades_functions import all_trades, create_trade, update_trade
from models.order import Orders
from models.trades import Trades
from schemas.trades_schemas import CreateTrade, UpdateTrade
from schemas.user_schemas import UserCreate
from utils.jicha_kereli import get_with_id_anything
from utils.role_aniqlovchi import role_admin

trade_router = APIRouter(tags=["Trades"])

@trade_router.get("/get_trades")
def hamma_tradelar(search: str = None, id: int = 0, page: int = 0, limit: int = 10, db: Session = Depends(get_db),
              request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Trades, id)
    return all_trades(search, page, limit, db)

@trade_router.post("/create_trade")
def trade_ochish(yangi_trade: CreateTrade, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    create_trade(yangi_trade, db, request_user)
    
    raise HTTPException(status_code=200, detail="Trade ochildi")

@trade_router.put("/update_trade")
def tradeni_yangilash(shu_tradeni: UpdateTrade, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_trade(shu_tradeni,db,request_user)
    raise HTTPException(status_code=200, detail="Trade yangilandi")
