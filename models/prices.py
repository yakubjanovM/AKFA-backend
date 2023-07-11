from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.maxsulot import Maxsulot



class Prices(Base):
    __tablename__ = "prices"
    id = Column(Integer, autoincrement=True, primary_key=True)
    price = Column(Numeric)
    # width1 = Column(Numeric)
    # width2 = Column(Numeric)
    # height1 = Column(Numeric)
    # height2 = Column(Numeric)
    maxsulot_id = Column(Integer)


    maxsulot = relationship('Maxsulot', foreign_keys=[maxsulot_id],
    primaryjoin=lambda: and_(Maxsulot.id == Prices.maxsulot_id))
