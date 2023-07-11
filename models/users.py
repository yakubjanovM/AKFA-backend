from database import Base
from sqlalchemy import *



class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(999))
    username = Column(String(999))
    password = Column(String(999))
    telefon_raqami = Column(Integer)
    role = Column(String(999))
    status = Column(Boolean)