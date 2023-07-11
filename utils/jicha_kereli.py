from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import Base


def get_with_id_anything(
        db: Session,
        model,
        id: int
):
    data = db.query(model).get(id)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{data} yoq"
        )
    return data


def save_qiladi(
        db: Session,
        data: Base
):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def yangiledi(
        db: Session,
        data: Base
):
    db.commit()
    db.refresh(data)
    return data
