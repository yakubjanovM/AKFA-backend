from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.order import Orders
class Nasiya(Base):
    __tablename__ = "nasiya"
    id = Column(Integer, autoincrement=True, primary_key=True)
    money = Column(Integer)
    qoldiq = Column(Integer)
    status = Column(Boolean)
    order_id = Column(Integer)
    
    order = relationship('Orders', foreign_keys=[order_id],
                              primaryjoin=lambda: and_(Orders.id == Nasiya.order_id))