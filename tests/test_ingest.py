from recall_ai.api.server import create_app
from fastapi.testclient import TestClient


def test_ingest():
    app = create_app()
    client = TestClient(app)
    payload = {"text": "test"}
    response = client.post("/ingest", json=payload)
    assert response.status_code == 202
    assert response.json() == {"accepted": True}
