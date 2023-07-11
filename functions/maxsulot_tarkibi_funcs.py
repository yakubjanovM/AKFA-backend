from models.maxsulot import Maxsulot
from models.olchov import Olchov
from utils.jicha_kereli import save_qiladi, get_with_id_anything
from utils.paginatsiya import pagination
from models.maxsulot_tarkibi import Maxsulot_tarkibi


def all_tarkiblar(search, page, limit, maxsulot_id, db):
    tarkiblar = db.query(Maxsulot_tarkibi)
    if search:
        search_formatted = "%{}%".format(search)
        tarkiblar = tarkiblar.filter(Maxsulot_tarkibi.name.like(search_formatted))
    if maxsulot_id:
        tarkiblar = tarkiblar.filter(Maxsulot_tarkibi.maxsulot_id == maxsulot_id)
    tarkiblar = tarkiblar.order_by(Maxsulot_tarkibi.name.asc())
    return pagination(tarkiblar, page, limit)


def create_tarkib(data, db):
    if get_with_id_anything(db, Maxsulot, data.maxsulot_id):
        olchov = db.query(Olchov).filter(Olchov.id == data.olchov_birligi).first()
        new_tarkib = Maxsulot_tarkibi(
            name=data.name,
            comment=data.comment,
            maxsulot_id=data.maxsulot_id,
            olchov_birligi=data.olchov_birligi, #olchov.name
            nechtaligi=data.nechtaligi
        )
        save_qiladi(db, new_tarkib)


def update_tarkib(data, db):
    if get_with_id_anything(db, Maxsulot_tarkibi, data.id):
        db.query(Maxsulot_tarkibi).filter(Maxsulot_tarkibi.id == data.id).update({
            Maxsulot_tarkibi.name: data.name,
            Maxsulot_tarkibi.comment: data.comment,
            Maxsulot_tarkibi.nechtaligi: data.nechtaligi
        })
        db.commit()

