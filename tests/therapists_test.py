import sys
import os

# Add the backend directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from backend.main import app
from backend.database import SessionLocal
import pytest

from sqlalchemy import text


client = TestClient(app)

from sqlalchemy.orm import Session

def reset_therapist_table(db: Session):
    db.execute(text(f"DELETE FROM therapists;"))
    db.commit()

# Then call this function in your test setup
db = SessionLocal()
reset_therapist_table(db)


def test_create_therapist():
    response = client.post(
        '/register/',
        json={'username': 'Skylar Presta', 'email': 'cool_babe18@hotmail.net', 'password': 'luna'}
    )
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'username': 'Skylar Presta', 'email': 'cool_babe18@hotmail.net'}

def test_get_therapists():
    response = client.get('/therapists/')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0