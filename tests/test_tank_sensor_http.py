import pytest
from lib.http_server import start_http_server

def test_read_and_calibrate_level():
    client = start_http_server("http://192.168.1.23/api")

    # Get current level
    response = client.get("/level")
    assert response.status_code == 200
    assert "level" in response.json()

    # Calibrate sensor
    response = client.post("/calibrate", json={"reference_level": 100})
    assert response.status_code == 200
    assert response.json().get("status") == "calibrated"
