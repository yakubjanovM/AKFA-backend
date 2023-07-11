from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

engine = create_engine('mysql+pymysql://root@localhost:3306/akfa')
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
print("DATABASE CONNECTED")