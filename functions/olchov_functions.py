from models.olchov import Olchov
from utils.jicha_kereli import save_qiladi, get_with_id_anything
from utils.paginatsiya import pagination



def all_olchovlar(search, page, limit, db):
    olchovlar = db.query(Olchov)
    if search:
        search_formatted = "%{}%".format(search)
        olchovlar = olchovlar.filter(Olchov.name.like(search_formatted))
    olchovlar = olchovlar.order_by(Olchov.name.asc())
    return pagination(olchovlar, page, limit)


def create_olchov(data, db, thisuser):
    yangi_olchov = Olchov(
        name=data.name
    )
    save_qiladi(db, yangi_olchov)


def update_olchov(data, db, thisuser):
    get_with_id_anything(db, Olchov, data.id)
    olchov = db.query(Olchov).filter(Olchov.id == data.id).update({
        Olchov.name: data.name
    })
    save_qiladi(db,olchov)#or db.commit








