from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

from database import Base


class UserCreate(BaseModel):
    username: str
    password: str
    name: str
    role: str
    telefon_raqami: int
    status: bool


class UserLogin(BaseModel):
    username: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    name: str
    username: str
    password: str
    telefon_raqami: int
    role: str
