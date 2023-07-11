from pydantic import BaseModel


class Createnarx(BaseModel):
    price: float
    # width1: float
    # width2: float
    # height1: float
    # height2: float
    maxsulot_id: int

class Updatenarx(BaseModel):
    id: int
    price: float