from fastapi import status,HTTPException,APIRouter
from functions.hasher_tekshiradi import hasher
from functions.token import get_current_user
from models.users import Users
from models.customers import Customers
from utils.paginatsiya import pagination
def create_customer(customer,db,user_logged):
    new_customer = Customers(
        name = customer.name,
        telefon_raqami = customer.telefon_raqami,
        user_id = user_logged.id
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
  
    return new_customer

def get_customer(id,db):
    customer = db.query(Customers).filter(Customers.id == id).first()
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Customer with id: {id} not found")
    return customer

def update_customer(yangilangan_customer,db,current_user):
    customer_query = db.query(Customers).filter(Customers.id == yangilangan_customer.id)
    customer = customer_query.first()
    if customer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id: {yangilangan_customer.id} does not exist")
    if customer.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized")
    # customer_query.update(yangilangan_customer.dict(),synchronize_session=False)
    # db.commit()
    db.query(Customers).filter(Customers.id == yangilangan_customer.id).update({
        Customers.name: yangilangan_customer.name,
        Customers.telefon_raqami: yangilangan_customer.telefon_raqami
    })
    db.commit()
    return customer_query.first()

# def every_customers(search, page, limit, db):
#     customers = db.query(Customers).all()
#     print(customers)
#     if search:
#         search_formatted = "%{}%".format(search)
#         customers = customers.filter(Customers.name.like(search_formatted))
#     customers = customers.order_by(Customers.name.asc())
#     return pagination(customers, page, limit)
def every_customers(search, page, limit, db):
    query = db.query(Customers)
    
    # apply search filter if necessary
    if search:
        query = query.filter(Customers.name.like(f'%{search}%'))
    
    # order the query by customer name
    query = query.order_by(Customers.name.asc())
    
    # calculate offset and limit based on page and limit values
    offset = (page - 1) * limit
    if offset < 0:
        offset = 0
    query = query.offset(offset).limit(limit)
    
    return query.all()

