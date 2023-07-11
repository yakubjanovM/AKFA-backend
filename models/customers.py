from sqlalchemy.orm import relationship

from database import Base
from sqlalchemy import *

from models.users import Users


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(999))
    telefon_raqami = Column(Integer)
    user_id = Column(Integer)

    user = relationship('Users', foreign_keys=[user_id],
                              primaryjoin=lambda: and_(Users.id == Customers.user_id))