from fastapi import HTTPException
from models.nasiya import Nasiya
from utils.jicha_kereli import save_qiladi
from utils.paginatsiya import pagination
import importlib

# Import the module dynamically
kirim_functions = importlib.import_module('functions.kirim_functions')

# Call the update_kirim function



def all_nasiya(search, page, limit, db):
    nasiyalar = db.query(Nasiya).join(Nasiya.order)
    if search:
        search_formatted = "%{}%".format(search)
        # nasiyalar = nasiyalar.filter(Users.name.like(search_formatted) | Users.username.like(search_formatted) | Customers.name.like(search_formatted))
    nasiyalar = nasiyalar.order_by(Nasiya.money.asc())
    return pagination(nasiyalar, page, limit)
def create_nasiya(money,qoldiq,order_id,db):
    yangi_nasiya = Nasiya(
        money = money,
        qoldiq= qoldiq,
        status=True,
        order_id = order_id
    )
    save_qiladi(db, yangi_nasiya)
def update_nasiya(data,db):
    nasiya = db.query(Nasiya).filter(Nasiya.id == data.id).first()
    yangi_qoldiq = nasiya.qoldiq - data.money
    if nasiya.qoldiq == data.money:
        db.query(Nasiya).filter(Nasiya.id == data.id).update({
        Nasiya.money: data.money,
        Nasiya.qoldiq: 0,
        Nasiya.status: False
    })
        kirim_functions.update_kirim(data,db)
        db.commit()
        raise HTTPException(status_code=200, detail="Nasiyani hammasi tolandi")
    else:
        db.query(Nasiya).filter(Nasiya.id == data.id).update({
        Nasiya.money: data.money,
        Nasiya.qoldiq: yangi_qoldiq,
        Nasiya.status: True
    })
        kirim_functions.update_kirim(data,db)
        db.commit()
        raise HTTPException(status_code=200, detail="Nasiya ni bir qismi  tolandi")


