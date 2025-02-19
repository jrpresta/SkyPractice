
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


class ClientCreate(BaseModel):
    name: str
    contact_info: str

    class Config:
        orm_mode = True


class ClientReturn(BaseModel):
    id: int
    name: str
    contact_info: str


class NoteCreate(BaseModel):
    content: str
    timestamp: str


class NoteReturn(BaseModel):
    id: int

    class Config:
        orm_mode = True