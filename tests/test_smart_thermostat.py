import pytest
from lib.mqtt_client import MqttClient

def test_set_temperature_via_mqtt():
    client = MqttClient(broker="192.168.1.23", port=1883)
    client.connect()

    topic_cmd = "thermostat/device123/cmd"
    topic_status = "thermostat/device123/status"

    client.publish(topic_cmd, '{"set_temp": 23}')
    status = client.wait_for_message(topic_status, timeout=5)

    assert status is not None
    assert '"current_temp": 23' in status

    client.disconnect()
