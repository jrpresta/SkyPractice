import sys
import os

# Add the backend directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.models import Client

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend.main import app
from backend.database import get_db
from backend.schemas import TherapistCreate, ClientCreate

client = TestClient(app)

def get_test_db():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def create_therapist():
    """Fixture to create a therapist, needed for client"""
    new_therapist = TherapistCreate(
        username='test_therapist',
        email='skyman18@yahoo.com',
        password='password123'
    )

    response = client.post('/register/', json=new_therapist.dict())
    assert response.status_code == 200


def test_create_client(create_therapist, db: Session):
    therapist_id = create_therapist['id']

    client_data = ClientCreate(
        name='Jack Bearsley',
        therapist_id = therapist_id
    )

    response = client.post('/clients/', json=client_data.dict())

    assert response.status_code == 200
    client_response = response.json()
    assert client_response['name'] == 'Jack Bearsley'
    assert client_response['therapist_id'] == therapist_id

    db_client = db.query(Client).filter(Client.id == client_response['id']).first()
    assert db_client is not None
    assert db_client.name == 'Jack Bearsley'
    assert db_client.therapist_id == therapist_id

    db.delete(db_client)
    db.commit()