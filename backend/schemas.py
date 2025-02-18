
from pydantic import BaseModel

class TherapistCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True