from fastapi import Depends,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.olchov_functions import all_olchovlar, create_olchov, update_olchov
from models.olchov import Olchov
from functions.token import get_current_user
from schemas.olchov_schemas import CreateOlchov, UpdateOlchov
from utils.jicha_kereli import get_with_id_anything
from schemas.user_schemas import UserCreate
from database import get_db
from utils.role_aniqlovchi import role_admin

olchov_router = APIRouter(
    prefix='/olchovlar',
    tags=["O`lchov"]
)


@olchov_router.get("/hamma_olchovlar")
def hamma_olchovlar(search: str = None, id: int = 0, page: int = 0, limit: int = 10, db: Session = Depends(get_db),
              request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Olchov, id)
    return all_olchovlar(search, page, limit, db)


@olchov_router.post("/olchov_ochish")
def olchovlar_ochish(yangi_olchov: CreateOlchov, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    create_olchov(yangi_olchov, db, request_user)
    raise HTTPException(status_code=200, detail="olchov ochildi")


@olchov_router.put("/olchov_yangilash")
def olchov_yangilash(shu_olchov: UpdateOlchov, db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_olchov(shu_olchov, db, request_user)
    raise HTTPException(status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")


