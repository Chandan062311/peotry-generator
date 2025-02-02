import pytest
import requests
import os
from app import app

def test_server_running():
    """Test if server is running and accessible"""
    try:
        # Allow for connection retries
        for _ in range(3):
            try:
                response = requests.get('http://localhost:8000', timeout=5)
                assert response.status_code == 200
                return
            except requests.ConnectionError:
                continue
        pytest.fail("Server is not running")
    except Exception as e:
        pytest.fail(f"Server test failed: {str(e)}")

def test_production_config():
    """Test if application is running with production config"""
    assert not app.config.get('DEBUG', True)
    assert app.config.get('ENV') == 'production'

def test_static_files():
    """Test if static files are being served"""
    with app.test_client() as client:
        css = client.get('/static/css/style.css')
        js = client.get('/static/js/script.js')
        assert css.status_code == 200
        assert js.status_code == 200

def test_poem_generation_production():
    """Test if poem generation works in production"""
    with app.test_client() as client:
        response = client.post('/', data={'prompt': 'Test deployment'})
        assert response.status_code == 200
        assert b'generated_text' in response.data