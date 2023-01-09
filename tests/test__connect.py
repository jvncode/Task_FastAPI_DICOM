from fastapi.testclient import TestClient
from main import app


def test_server_reconnect():
    client = TestClient(app)
    response = client.get('/reconnect')
    assert response.status_code == 200, response.text


def test_server_patient():
    client = TestClient(app)
    response = client.get('/patient')
    assert response.status_code == 200, response.text
