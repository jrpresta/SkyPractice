
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.database import Base


class Therapist(Base):
    __tablename__ = 'therapists'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

    clients = relationship("Client", back_populates="therapist")

    def __repr__(self):
        return f'<Therapist(username={self.name}, email={self.email})>'


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_info = Column(String)
    therapist_id = Column(Integer, ForeignKey('therapists.id'))

    therapist = relationship("Therapist", back_populates="clients")
    notes = relationship("Note", back_populates="client")


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    timestamp = Column(DateTime)
    client_id = Column(Integer, ForeignKey('clients.id'))

    client = relationship("Client", back_populates="notes")