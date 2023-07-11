from jose import JWTError,jwt 
from datetime import datetime,timedelta
from database import get_db
from schemas.token_schemas import TokenData
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config import settings
from models.users import Users
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_acces_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
def verify_acces_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data = TokenData(id=id)
    except JWTError:
        raise credentials_exception
    return token_data
def get_current_user(token: str=Depends(oauth2_scheme),db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Could not Validate Creditionals",headers={"WWW-Authenticate": "Bearer"})

    token = verify_acces_token(token,credentials_exception)
    user = db.query(Users).filter(Users.id == token.id).first()
    return user
