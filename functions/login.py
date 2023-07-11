
from fastapi import Depends, HTTPException,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from functions.token import create_acces_token
from database import SessionLocal
from database import get_db
from models.users import Users
# from functions.hasher_tekshiradi import tekshiradi
def login(user_credentials: OAuth2PasswordRequestForm = Depends(),db: SessionLocal = Depends(get_db)):
    user = db.query(Users).filter(Users.username ==  user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this: {user_credentials.username} not found")
    
    # if not tekshiradi(user_credentials.password,user.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with this password: {user_credentials.password} is wrong")
    acces_token = create_acces_token(data={"user_id": user.id})
    return {'access_token':acces_token,"token_type":"bearer"}