from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session
from functions.login import login
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from database import SessionLocal
from database import get_db

auth_router = APIRouter(tags=['Authentication'])

@auth_router.post('/login')
def create_login(user_credentials: OAuth2PasswordRequestForm = Depends(),db: SessionLocal = Depends(get_db)):
    return  login(user_credentials,db)
