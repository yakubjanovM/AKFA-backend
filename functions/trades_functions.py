from sqlalchemy.orm import joinedload
from functions.order_funcs import update_order
from models.maxsulot import Maxsulot
from models.maxsulot_tarkibi import Maxsulot_tarkibi
from models.trades import Trades
from models.users import Users
from utils.jicha_kereli import get_with_id_anything, save_qiladi
from utils.paginatsiya import pagination


def all_trades(search, page, limit, db):
    tradelar = db.query(Trades).join(Trades.user).options(joinedload(Trades.user))
    if search:
        search_formatted = "%{}%".format(search)
        tradelar = tradelar.filter(Users.name.like(search_formatted) | Users.username.like(search_formatted) | Maxsulot.name.like(search_formatted) | Maxsulot_tarkibi.name.like(search_formatted))
    tradelar = tradelar.order_by(Trades.quantity.asc())
    return pagination(tradelar, page, limit)

def create_trade(data, db, thisuser):
    # get_with_id_anything(db, Trades, data.order_id)
    yangi_trade = Trades(
        maxsulot_id=data.maxsulot_id,
        width=data.width,
        height=data.height,
        quantity=data.quantity,
        order_id=data.order_id,
        user_id=thisuser.id
    )
    save_qiladi(db, yangi_trade)

def update_trade(data, db, thisuser):
    get_with_id_anything(db, Trades, data.id),
    # # get_with_id_anything(db, Trades, data.order_id)
    # if db.query(Orders).filter(Orders.id == data.id).first().status == "2":
    #     raise HTTPException(status_code=400, detail=f"Bu id: {data.id} dagi order  bajarildi!")
    # if db.query(Orders).filter(Orders.id == data.id).first().status == "0" and data.status != "0" and data.status != "1":
    #     raise HTTPException(status_code=400, detail="Bu order statusi 0 ga yani false ga teng siz xozir buni faqat 0 yoki 1 yani bajarilmoqda ga ozgartirishingiz mumkin")
    # if db.query(Orders).filter(Orders.id == data.id).first().status == "1" and data.status != "0" and data.status != "1" and data.status != "2":
    #     raise HTTPException(status_code=400,
    #                         detail="Bu order xozir 1 yani bajarilmoqdaga teng uni 0 yoki 1ligicha yoki 2 bajarildi ga ozgartirishingiz mumkin")
    ##.filter(Trades.user == thisuser.id).first()
    db.query(Trades).filter(Trades.id == data.id).update({
        Trades.width: data.width,
        Trades.height: data.height,
        Trades.quantity: data.quantity
    })
    db.commit()

