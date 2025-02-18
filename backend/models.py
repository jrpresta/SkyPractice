
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base


class Therapist(Base):
    __tablename__ = 'therapists'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def __repr__(self):
        return f'<Therapist(username={self.name}, email={self.email})>'