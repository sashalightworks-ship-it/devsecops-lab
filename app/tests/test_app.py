from app import app

def test_index_returns_message():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "message" in resp.get_json()

def test_health_is_ok():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}