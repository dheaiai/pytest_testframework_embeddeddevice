
import pytest
from lib.ssh_client import SSHClient

def test_read_device_config_ssh():
    ssh = SSHClient(host="192.168.1.23", username="admin", password="admin123")
    ssh.connect()

    output = ssh.execute("cat /etc/device_config.json")
    assert '"device_type": "smart_lock"' in output

    ssh.disconnect()
