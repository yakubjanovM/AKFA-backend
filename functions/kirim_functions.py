from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import joinedload
from models.kirim import Kirim
from models.prices import Prices
from models.trades import Trades
from models.users import Users
from utils.jicha_kereli import get_with_id_anything, save_qiladi
from utils.paginatsiya import pagination
from functions.nasiya_functions import create_nasiya


def all_kirimlar(search, page, limit, db):
    kirimlar = db.query(Kirim).join(Kirim.source).join(Kirim.user).options(joinedload(Kirim.source), joinedload(Kirim.user))
    if search:
        search_formatted = "%{}%".format(search)
        kirimlar = kirimlar.filter(Users.name.like(search_formatted) | Users.username.like(search_formatted))
    kirimlar = kirimlar.order_by(Kirim.money.asc())
    return pagination(kirimlar, page, limit)


def create_kirim(data, db, thisuser):
    shu_tradega = db.query(Trades).filter(Trades.order_id == data.source_id).first()
    price = db.query(Prices).filter(Prices.maxsulot_id == shu_tradega.maxsulot_id).first()
    
    money = price.price * shu_tradega.quantity
    qoldiq = money - data.money
    if qoldiq != 0 and qoldiq > 0:
        create_nasiya(data.money,qoldiq,data.source_id,db)
        raise HTTPException(status_code=200, detail="Pulingiz kam bolgani tufayli nasiya ochildi")
    else:
        yangi_kirim = Kirim(
            money = money,
            time = datetime.now(),
            source_id = data.source_id,
            user_id=thisuser.id,
        )
        save_qiladi(db, yangi_kirim)
        raise HTTPException(status_code=200, detail="Kirim ochildi")

def update_kirim(data, db):
    
    get_with_id_anything(db, Kirim, data.id)

    db.query(Kirim).filter(Kirim.id == data.id).update({
        Kirim.money: data.money,
        Kirim.time: datetime.now()
    })
    db.commit()
