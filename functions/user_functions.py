from fastapi import status,HTTPException,APIRouter
from functions.hasher_tekshiradi import hasher
from models.users import Users

def create_user(user,db):
    hashed_password = hasher(user.password)
    user.password = hashed_password
    new_user = Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
  
    return new_user

def get_user(id,db):
    user = db.query(Users).filter(Users.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id: {id} not found")
    return user

def update_user(id, yangilangan_user,db,current_user):
    user_query = db.query(Users).filter(Users.id == id)
    user = user_query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    if user.id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
    user_query.update(yangilangan_user.dict(),synchronize_session=False)
    db.commit()
    return user_query.first()

def every_users(search, page, limit, db):
    query = db.query(Users)
    
    # apply search filter if necessary
    if search:
        query = query.filter(Users.name.ilike(f'%{search}%'))
    
    # order the query by customer name
    query = query.order_by(Users.name.asc())
    
    # calculate offset and limit based on page and limit values
    offset = (page - 1) * limit
    if offset < 0:
        offset = 0
    query = query.offset(offset).limit(limit)
    
    return query.all()
