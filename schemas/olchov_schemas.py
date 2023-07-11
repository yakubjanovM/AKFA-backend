from pydantic import BaseModel


class CreateOlchov(BaseModel):
    name: str

class UpdateOlchov(BaseModel):
    id: int
    name: str
