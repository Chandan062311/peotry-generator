from app import app

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_poem_generation():
    client = app.test_client()
    response = client.post('/', data={'prompt': 'Test prompt'})
    assert response.status_code == 200