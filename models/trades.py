from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

from models.order import Orders
from models.users import Users
from models.maxsulot import Maxsulot

class Trades(Base):
    __tablename__ = "trades"
    id = Column(Integer, autoincrement=True, primary_key=True)
    maxsulot_id = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)
    quantity = Column(Integer)
    order_id = Column(Integer)
    user_id = Column(Integer)
    
    
    maxsulot = relationship('Maxsulot', foreign_keys=[maxsulot_id],
                              primaryjoin=lambda: and_(Maxsulot.id == Trades.maxsulot_id))
    
    user = relationship('Users', foreign_keys=[user_id],
                              primaryjoin=lambda: and_(Users.id == Trades.user_id))
    
    order = relationship('Orders', foreign_keys=[order_id],
                              primaryjoin=lambda: and_(Orders.id == Trades.order_id))