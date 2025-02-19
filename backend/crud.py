
from sqlalchemy.orm import Session
from backend.models import Therapist
from backend.schemas import TherapistCreate

def create_therapist(db: Session, therapist: TherapistCreate):
    db_therapist = Therapist(
        username=therapist.username,
        email = therapist.email,
        password_hash=therapist.password
    )

    db.add(db_therapist)
    db.commit()
    db.refresh(db_therapist)
    return db_therapist


def create_client(db: Session, client):
    db_client = Client(
        name=client.name,
        contact_info=client.contact_info,
        therapist_id=client.therapist_id
    )

    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_note(db: Session, note, client_id):
    pass
    db_note = Note(
        content=note.content,
        timestamp=note.timestamp,
        client_id=client_id
    )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note