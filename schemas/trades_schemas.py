from pydantic import BaseModel

class CreateTrade(BaseModel):
    maxsulot_id: int
    width: float
    height: float
    quantity: float
    order_id: int
    user_id: int


class UpdateTrade(BaseModel):
    id: int
    width: float
    height: float
    quantity: float
    