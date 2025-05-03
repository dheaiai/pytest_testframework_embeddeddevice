import json
from utils.terminal_util import run_cmd

def test_device_ping():
    with open("../config/config_dev1.json") as f:
        config = json.load(f)
    response = run_cmd(f"ping -c 2 {config['device_ip']}")
    assert "bytes from" in response
