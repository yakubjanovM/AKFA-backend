from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
import inspect
from functions.maxsulot_funcs import all_maxsulotlar, create_maxsulot, update_maxsulot
from models.maxsulot import Maxsulot
from schemas.user_schemas import UserCreate
from functions.token import get_current_user
from utils.role_aniqlovchi import role_admin
from utils.jicha_kereli import get_with_id_anything
from schemas.maxsulot_schemas import CreateMaxsulot,UpdateMaxsulot

maxsulot_router = APIRouter(tags=["Products"])

@maxsulot_router.get("/get_products")
def get_maxsulotlar(search: str = None,
                    id: int = 0,
                    page: int = 0,
                    limit: int = 10,
                    db: Session = Depends(get_db),
                    current_user: UserCreate = Depends(get_current_user)):
    role_admin(current_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Maxsulot, id)
    return all_maxsulotlar(search, page, limit, current_user, db)


@maxsulot_router.post("/create_product")
def create_main_maxsulot(new_material: CreateMaxsulot, db: Session = Depends(get_db),
                current_user: UserCreate = Depends(get_current_user)):
    role_admin(current_user)
    create_maxsulot(new_material,db)
    raise HTTPException(status_code=200, detail="Maxsulot muvaffaqiyatli qoshildi")



@maxsulot_router.put("/update_product")
def update_main_maxsulot(shu_maxsulot: UpdateMaxsulot, db: Session = Depends(get_db),
                current_user: UserCreate = Depends(get_current_user)):
    role_admin(current_user)
    update_maxsulot(shu_maxsulot, db)
    raise HTTPException(status_code=200, detail="Maxsulot muvaffaqiyatli yangilandi")