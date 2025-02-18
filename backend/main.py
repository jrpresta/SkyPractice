
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine
from backend import models, crud, schemas

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

@app.post('/register/')
def register_therapist(therapist: schemas.TherapistCreate, db: Session = Depends(get_db)):
    db_therapist = crud.create_therapist(db=db, therapist=therapist)
    return {"id": db_therapist.id, "username": db_therapist.username, "email": db_therapist.email}

def main():
    # db = get_db()
    return

if __name__ == '__main__':
    print(main())