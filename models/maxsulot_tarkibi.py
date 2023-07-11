from database import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.maxsulot import Maxsulot
from models.olchov import Olchov
class Maxsulot_tarkibi(Base):
    __tablename__ = "maxsulot_tarkibi"
    id = Column(Integer, primary_key=True)
    name = Column(String(999))
    nechtaligi = Column(Integer)
    comment = Column(String(999))
    maxsulot_id = Column(Integer)
    status = Column(Boolean)
    olchov_birligi = Column(Integer)
    
    maxsulot = relationship('Maxsulot', foreign_keys=[maxsulot_id],
                              primaryjoin=lambda: and_(Maxsulot.id == Maxsulot_tarkibi.maxsulot_id))
    
    olchov = relationship('Olchov', foreign_keys=[olchov_birligi],
                              primaryjoin=lambda: and_(Olchov.id == Maxsulot_tarkibi.olchov_birligi))