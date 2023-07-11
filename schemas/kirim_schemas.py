import datetime

from pydantic import BaseModel


class CreateKirim(BaseModel):
    money: int
    time: datetime.date
    source_id: int
    user_id: int
 

class UpdateKirim(BaseModel):
    id: int
    money: int
    time: datetime.date
