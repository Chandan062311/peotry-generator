
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Poetry Generator' in response.data

def test_poem_generation(client):
    test_prompt = "Once upon a time"
    response = client.post('/', data={'prompt': test_prompt})
    assert response.status_code == 200
    assert response.data  # Verify response contains data

def test_empty_prompt(client):
    response = client.post('/', data={'prompt': ''})
    assert response.status_code == 200

def test_long_prompt(client):
    long_prompt = "a" * 1000
    response = client.post('/', data={'prompt': long_prompt})
    assert response.status_code == 200

def test_special_characters(client):
    special_prompt = "!@#$%^&*()"
    response = client.post('/', data={'prompt': special_prompt})
    assert response.status_code == 200