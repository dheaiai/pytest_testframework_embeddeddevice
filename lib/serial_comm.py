import serial
import yaml
from utils.logger import setup_logger

logger = setup_logger(__name__)

class SerialDriver:
    def __init__(self, config_path="config/device_config.yaml"):
        with open(config_path) as f:
            cfg = yaml.safe_load(f)
        self.port = cfg["serial_port"]
        self.baud = cfg["baud_rate"]
        self.ser = serial.Serial(self.port, self.baud, timeout=1)
        logger.info(f"Opened serial port {self.port} at {self.baud} baud")

    def write(self, data):
        self.ser.write(data.encode())
        logger.debug(f"Sent: {data}")

    def read(self):
        data = self.ser.readline().decode().strip()
        logger.debug(f"Received: {data}")
        return data
