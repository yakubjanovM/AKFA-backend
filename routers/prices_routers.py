from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.prices_funcs import all_narxlar, create_narx, update_narx
from functions.token import get_current_user
from models.prices import Prices
from schemas.prices_schemas import Createnarx, Updatenarx
from schemas.user_schemas import UserCreate
from utils.jicha_kereli import get_with_id_anything
from utils.role_aniqlovchi import role_admin

prices_router = APIRouter(tags=["Prices"])

@prices_router.get("/get_orices")
def hamma_narxlar(id: int = 0, page: int = 0, limit: int = 10, db: Session = Depends(get_db),
              request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Prices, id)
    return all_narxlar(page, limit, db)


@prices_router.post("/create_price")
def narx_berish(yangi_narx: Createnarx, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    create_narx(yangi_narx, db)
    raise HTTPException(status_code=200, detail="Narx qoshildi")


@prices_router.put("/update_price")
def narxni_yangilash(yangilanayotgan_narx: Updatenarx, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_narx(yangilanayotgan_narx, db)
    raise HTTPException(status_code=200, detail="Ushbu maxsulot narxi yangilandi")