from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.order import Orders
from models.users import Users

class Kirim(Base):
    __tablename__ = "kirim"
    id = Column(Integer, autoincrement=True, primary_key=True)
    money = Column(Integer)
    time = Column(DateTime)
    source_id = Column(Integer)
    user_id = Column(Integer)
    
    user = relationship('Users', foreign_keys=[user_id],
                              primaryjoin=lambda: and_(Users.id == Kirim.user_id))
    
    source = relationship('Orders', foreign_keys=[source_id],
                              primaryjoin=lambda: and_(Orders.id == Kirim.source_id))