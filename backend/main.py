
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine
from backend import models, crud, schemas

"""
Common Commands:
uvicorn backend.main:app --reload

alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
"""

# Create all the tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def read_root():
    return {"message": "Hello, therapist"}


@app.get("/therapists", response_model=list[schemas.TherapistReturn])
def get_therapists(db: Session = Depends(get_db)):
    therapists = db.query(models.Therapist).all()
    return therapists


@app.post('/register/')
def register_therapist(therapist: schemas.TherapistCreate, db: Session = Depends(get_db)):
    db_therapist = crud.create_therapist(db=db, therapist=therapist)
    return {"id": db_therapist.id, "username": db_therapist.username, "email": db_therapist.email}


@app.post('/clients/')
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.create_client(db=db, client=client)
    return {"id": db_client.id, "name": db_client.name, "contact_info": db_client.contact_info}


@app.post('/clients/{client_id}/notes/')
def create_note(client_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = crud.create_note(db=db, note=note, client_id=client_id)
    return {"id": db_note.id}


@app.get('/clients/{client_id}/notes/')
def get_notes(client_id: int, db: Session = Depends(get_db)):
    notes = crud.get_notes(db=db, client_id=client_id)
    return notes


def main():
    return

if __name__ == '__main__':
    print(main())

#     curl - X
#     'POST' \
#     'http://127.0.0.1:8000/register/' \
#     -H
#     'Content-Type: application/json' \
#     -d
#     '{
#     "username": "therapist1",
#     "email": "therapist1@example.com",
#     "password": "password123"
# }'
