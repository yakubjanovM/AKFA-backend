from pydantic import BaseModel

class CreateCustomer(BaseModel):
    name: str
    telefon_raqami: int
    user_id: int

class UpdateCustomer(BaseModel):
    id: int
    name: str
    telefon_raqami: int
