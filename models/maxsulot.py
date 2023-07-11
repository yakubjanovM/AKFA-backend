from database import Base
from sqlalchemy import *
from models.users import Users
from sqlalchemy.orm import relationship

class Maxsulot(Base):
    __tablename__ = "maxsulot"
    id = Column(Integer,autoincrement=True,primary_key=True)
    name = Column(String(999))
    comment = Column(String(999))
    user_id = Column(Integer)
    status = Column(Boolean,default=True)

    
    user = relationship('Users', foreign_keys=[user_id],
                              primaryjoin=lambda: and_(Users.id == Maxsulot.user_id))