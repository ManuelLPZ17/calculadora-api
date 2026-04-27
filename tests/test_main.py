from fastapi.testclient import TestClient
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app.main import app

client = TestClient(app)

def test_suma():
    r = client.get("/suma?a=3&b=2")
    assert r.status_code == 200
    assert r.json()["resultado"] == 5.0

def test_resta():
    r = client.get("/resta?a=10&b=4")
    assert r.status_code == 200
    assert r.json()["resultado"] == 6.0

def test_multiplicacion():
    r = client.get("/multiplicacion?a=3&b=4")
    assert r.status_code == 200
    assert r.json()["resultado"] == 12.0

def test_division():
    r = client.get("/division?a=10&b=2")
    assert r.status_code == 200
    assert r.json()["resultado"] == 5.0

def test_division_por_cero():
    r = client.get("/division?a=5&b=0")
    assert r.status_code == 400