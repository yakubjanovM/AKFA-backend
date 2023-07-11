from fastapi import HTTPException


def role_admin(user):
    if user.role == "admin":
        return True
    raise HTTPException(status_code=401, detail='Sizga ruhsat berilmagan!')


def role_operator(user):
    if user.role == "operator":
        return True
    raise HTTPException(status_code=401, detail='Sizga ruhsat berilmagan!')
    