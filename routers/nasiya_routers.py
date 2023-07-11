from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from functions.nasiya_functions import all_nasiya, update_nasiya
from functions.token import get_current_user
from models.nasiya import Nasiya
from schemas.nasiya_schemas import UpdateNasiya
from schemas.user_schemas import UserCreate
from utils.jicha_kereli import get_with_id_anything
from utils.role_aniqlovchi import role_admin

nasiya_router = APIRouter(tags=["Nasiyalar"])
 
@nasiya_router.get("/get_nasiyalar")
def hamma_nasiyalar(search: str = None, id: int = 0, page: int = 0, limit: int = 10, db: Session = Depends(get_db),
              request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db, Nasiya, id)
    return all_nasiya(search, page, limit, db)

@nasiya_router.put("/update_nasiya")
def nasiyani_yangilash(yangilanayotgan_nasiya: UpdateNasiya, db: Session = Depends(get_db),
              request_user: UserCreate = Depends(get_current_user)):
    role_admin(request_user)
    update_nasiya(yangilanayotgan_nasiya,db)
    