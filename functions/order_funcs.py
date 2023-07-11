from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models.customers import Customers
from models.users import Users
from utils.jicha_kereli import save_qiladi, get_with_id_anything
from utils.paginatsiya import pagination
from models.order import Orders


def all_orders(search, page, limit, db):
    orderlar = db.query(Orders).join(Orders.customer).join(Orders.user).options(joinedload(Orders.customer), joinedload(Orders.user))
    if search:
        search_formatted = "%{}%".format(search)
        orderlar = orderlar.filter(Users.name.like(search_formatted) | Users.username.like(search_formatted) | Customers.name.like(search_formatted))
    orderlar = orderlar.order_by(Orders.status.asc())
    return pagination(orderlar, page, limit)


def create_order(data, db, thisuser):
    get_with_id_anything(db, Customers, data.customer_id)
    yangi_order = Orders(
        customer_id=data.customer_id,
        status="0",#false,
        user_id=thisuser.id,
        time=datetime.now()
    )
    save_qiladi(db, yangi_order)


def update_order(data, db, thisuser):
    get_with_id_anything(db, Orders, data.id)
    if db.query(Orders).filter(Orders.id == data.id).first().status == "2":
        raise HTTPException(status_code=400, detail=f"Bu id: {data.id} dagi order  bajarildi!")
    if db.query(Orders).filter(Orders.id == data.id).first().status == "0" and data.status != "0" and data.status != "1":
        raise HTTPException(status_code=400, detail="Bu order statusi 0 ga yani false ga teng siz xozir buni faqat 0 yoki 1 yani bajarilmoqda ga ozgartirishingiz mumkin")
    if db.query(Orders).filter(Orders.id == data.id).first().status == "1" and data.status != "0" and data.status != "1" and data.status != "2":
        raise HTTPException(status_code=400,
                            detail="Bu order xozir 1 yani bajarilmoqdaga teng uni 0 yoki 1ligicha yoki 2 bajarildi ga ozgartirishingiz mumkin")
    db.query(Orders).filter(Orders.id == data.id).update({
        Orders.status: data.status,
        Orders.time: datetime.now()
    })
    db.commit()


def delete_order(id, db):
    get_with_id_anything(db, Orders, id)
    db.query(Orders).filter(Orders.id == id).delete()
    db.commit()







