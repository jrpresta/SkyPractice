
from fastapi import FastAPI
from backend.database import engine

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello, therapist"}
