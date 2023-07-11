from pydantic import BaseModel


class CreateMaxsulot(BaseModel):
    name: str
    comment: str
    user_id: int

class UpdateMaxsulot(BaseModel):
    id: int
    name: str
    comment: str