from utils.jicha_kereli import get_with_id_anything,save_qiladi,yangiledi
from utils.paginatsiya import pagination
from models.maxsulot import Maxsulot

def all_maxsulotlar(search, page, limit, current_user, db):
    maxsulotlar = db.query(Maxsulot)
    if search:
        search_formatted = "%{}%".format(search)
        maxsulotlar = maxsulotlar.filter(Maxsulot.name.like(search_formatted))
    if current_user:
        maxsulotlar = maxsulotlar.filter(Maxsulot.user_id == current_user.id)
    maxsulotlar = maxsulotlar.order_by(Maxsulot.name.asc())
    return pagination(maxsulotlar, page, limit)

def create_maxsulot(data, db):
    yangi_maxsulot_db = Maxsulot(
        name=data.name,
        comment=data.comment,
        user_id=data.user_id
    )
    save_qiladi(db, yangi_maxsulot_db)

def update_maxsulot(data, db):
        if get_with_id_anything(db, Maxsulot, data.id):
            db.query(Maxsulot).filter(Maxsulot.id == data.id).update({
                Maxsulot.name: data.name,
                Maxsulot.comment: data.comment
            })
            db.commit()
