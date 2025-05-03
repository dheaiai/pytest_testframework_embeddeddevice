import pytest
from lib.websocket_client import WebSocketClient
import json

def test_receive_location_over_websocket():
    ws = WebSocketClient("ws://192.168.1.55:8080/gpsstream")
    ws.connect()

    message = ws.receive(timeout=5)
    assert message is not None

    data = json.loads(message)
    assert "latitude" in data and "longitude" in data

    ws.close()
