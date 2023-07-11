from fastapi import Depends, FastAPI,Response,status,HTTPException,APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from models.users import Users
from schemas.user_schemas import UserOut,UserCreate,UserUpdate
from functions.user_functions import create_user, every_users,get_user, update_user
from functions.token import get_current_user
from utils.jicha_kereli import get_with_id_anything
from utils.role_aniqlovchi import role_admin

user_router = APIRouter(tags=["Users"])

@user_router.get("/get_users")
def get_all(search: str = None,
            id: int = 0,
            page: int = 0,
            limit: int = 25,
            db: Session= Depends(get_db),
            current_user: UserCreate = Depends(get_current_user)):
    role_admin(current_user)
    if page < 0 or limit < 0:
        raise HTTPException(status_code=400, detail=status.HTTP_400_BAD_REQUEST)
    if id > 0:
        return get_with_id_anything(db,Users,id)
    return every_users(search, page, limit, db)

@user_router.get("/get_user/{id}",response_model=UserOut)
def get_by_id(id: int,db: Session = Depends(get_db)):
    return get_user(id,db)

@user_router.post("/create_user",status_code=status.HTTP_201_CREATED,response_model=UserOut)
def user_create(user:UserCreate, db:Session = Depends(get_db)):
    return create_user(user,db)

@user_router.put("/update_user/{id}",response_model=UserUpdate,status_code=status.HTTP_202_ACCEPTED)
def user_update(id:int,updated_user: UserCreate,db: Session = Depends(get_db),current_user: int = Depends(get_current_user)):
    return update_user(id,updated_user,db,current_user)