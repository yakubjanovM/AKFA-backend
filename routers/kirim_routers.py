from fastapi import Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.kirim_functions import all_kirimlar, create_kirim, update_kirim
from functions.token import get_current_user
from models.kirim import Kirim
from schemas.kirim_schemas import CreateKirim, UpdateKirim
from schemas.user_schemas import UserOut, UserCreate, UserUpdate
from utils.jicha_kereli import get_with_id_anything
from utils.role_aniqlovchi import role_admin

kirim_router = APIRouter(tags=["Kirimlar"])


@kirim_router.get("/get_kirimlar")
def hamma_kirimlar(search: str = None, id: int = 0, page: int = 0, limit: int = 10, db: Session = Depends(get_db),
                   request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(
            status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Kirim, id)
    return all_kirimlar(search, page, limit, db)


@kirim_router.post("/kirim_ochish")
def kirim_ochish(yangi_kirim: CreateKirim, db: Session = Depends(get_db),
                 request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    create_kirim(yangi_kirim, db, request_user)
    raise HTTPException(status_code=200, detail="Kirim ochildi")


@kirim_router.put("/kirimni_yangilash")
def orderni_yangilash(shu_kirimni: UpdateKirim, db: Session = Depends(get_db),
                      request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_kirim(shu_kirimni, db, request_user)
    raise HTTPException(
        status_code=200, detail="Amaliyot muvaffaqiyatli amalga oshirildi")
