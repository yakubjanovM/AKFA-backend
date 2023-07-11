from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.maxsulot_tarkibi_funcs import all_tarkiblar, create_tarkib, update_tarkib
from functions.token import get_current_user
from models.maxsulot_tarkibi import Maxsulot_tarkibi
from schemas.maxsulot_tarkibi_shcemas import CreateTarkibi, UpdateTarkibi
from schemas.user_schemas import UserCreate
from utils.jicha_kereli import get_with_id_anything
from utils.role_aniqlovchi import role_admin

max_tarkibi_router = APIRouter(tags=["Maxsulot Tarkibi"])


@max_tarkibi_router.get("/get_maxsulot_tarkiblari")
def get_main_tarkiblari(
    search: str = None,
    id: int = 0,
    page: int = 0, 
    limit: int = 10, 
    maxsulot_id: int = None, 
    db: Session = Depends(get_db),
    request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Maxsulot_tarkibi, id)
    return all_tarkiblar(search, page, limit, maxsulot_id, db)


@max_tarkibi_router.post("/create_tarkib")
def tarkib_qoshish(yangi_tarkib: CreateTarkibi, 
                   db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    create_tarkib(yangi_tarkib, db)
    raise HTTPException(status_code=200, detail="Yangi tarkib qoshildi")


@max_tarkibi_router.put("/update_tarkib")
def tarkibni_yangilash(qaysi_tarkibni: UpdateTarkibi, 
                       db: Session = Depends(get_db),
                request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_tarkib(qaysi_tarkibni, db)
    raise HTTPException(status_code=200, detail="Tarkib yangilandi")