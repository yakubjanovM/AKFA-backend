from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.order import Orders
from models.users import Users

class Olchov(Base):
    __tablename__ = "olchov"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(999))
    