import pytest
from lib.serial_comm import SerialDriver
from utils.regex_util import extract_error_codes

def test_start_infusion_command():
    device = SerialDriver(port='/dev/ttyUSB0', baudrate=9600)
    device.open()

    device.send_command("START_INFUSION")
    output = device.read_until("INFUSION_STARTED", timeout=5)

    assert "INFUSION_STARTED" in output

    error_codes = extract_error_codes(output)
    assert not error_codes  # No error code should be found

    device.close()
