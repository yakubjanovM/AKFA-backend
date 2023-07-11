import datetime

from pydantic import BaseModel

# class CreateNasiya(BaseModel):
#     money: int
#     order_id: datetime.date
 

class UpdateNasiya(BaseModel):
    id: int
    money: int
