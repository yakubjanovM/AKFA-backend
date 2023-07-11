from models.kirim import Kirim
from models.prices import Prices
from models.trades import Trades
from models.users import Users
from utils.paginatsiya import pagination
from sqlalchemy.orm import joinedload
def all_statistics(db):
    top_kirim = db.query(Kirim).all()
    # for i in top_kirim:
    #     print(i.money)
    kirimlar = db.query(Kirim).join(Kirim.source).join(Kirim.user).options(joinedload(Kirim.source), joinedload(Kirim.user))
    kirimlar = kirimlar.order_by(Kirim.money.asc())
    return pagination(kirimlar)