
from pydantic import BaseModel

class TherapistCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class TherapistReturn(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True