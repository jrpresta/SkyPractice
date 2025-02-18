
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