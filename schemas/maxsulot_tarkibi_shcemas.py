from pydantic import BaseModel


class CreateTarkibi(BaseModel):
    name: str
    comment: str
    maxsulot_id: int
    olchov_birligi: int
    nechtaligi: int


class UpdateTarkibi(BaseModel):
    id: int
    name: str
    comment: str
    nechtaligi: int
