import os
import sys

# Make sure Python can find the 'app' package from the project root
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.app import app


def test_health_route():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert b"OK" in response.data

