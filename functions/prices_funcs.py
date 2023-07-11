from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload

from models.maxsulot import Maxsulot
from utils.jicha_kereli import save_qiladi, get_with_id_anything
from utils.paginatsiya import pagination
from models.prices import Prices


def all_narxlar(page, limit, db):
    # narxlar = db.query(Prices).join(Prices.maxsulot_id).options(joinedload(Prices.maxsulot_id)).order_by(Prices.price.asc())
    # return pagination(narxlar, page, limit)
    query = db.query(Prices)
    
    # apply search filter if necessary
    # if search:
    #     query = query.filter(Customers.name.ilike(f'%{search}%'))
    
    # # order the query by customer name
    # query = query.order_by(Customers.name.asc())
    
    # calculate offset and limit based on page and limit values
    offset = (page - 1) * limit
    if offset < 0:
        offset = 0
    query = query.offset(offset).limit(limit)
    
    return query.all()

def create_narx(data, db):
    if get_with_id_anything(db, Maxsulot, data.maxsulot_id):
        yangi_narx = Prices(
            price=data.price,
            # width1=data.width1,
            # width2=data.width2,
            # height1=data.height1,
            # height2=data.height2,
            maxsulot_id=data.maxsulot_id
        )
        save_qiladi(db, yangi_narx)


def update_narx(data, db):
    if get_with_id_anything(db, Prices, data.id):
        db.query(Prices).filter(Prices.id == data.id).update({
            Prices.price: data.price
        })
        db.commit()

