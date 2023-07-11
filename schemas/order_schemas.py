import datetime

from pydantic import BaseModel


class CreateOrder(BaseModel):
    customer_id: int
    time: datetime.date
 

class UpdateOrder(BaseModel):
    id: int
    status: str
    time: datetime.date

