import os
from env_utils import load_env_file, get_env_variable

# Load .env values into the environment
load_env_file()

class Config:
    # Environment
    ENV = get_env_variable("ENV", "production")
    LOG_LEVEL = get_env_variable("LOG_LEVEL", "INFO")
    LOG_FILE = get_env_variable("LOG_FILE", "logs/test_framework.log")

    # Device settings
    DEVICE_PORT = get_env_variable("DEVICE_PORT", "/dev/ttyUSB0")
    BAUD_RATE = int(get_env_variable("BAUD_RATE", 9600))

    # Timeouts
    CONNECTION_TIMEOUT = int(get_env_variable("CONNECTION_TIMEOUT", 5))
    TEST_TIMEOUT = int(get_env_variable("TEST_TIMEOUT", 20))

if __name__ == "__main__":
    print("Configuration Loaded:")
    print(f"ENV: {Config.ENV}")
    print(f"LOG_LEVEL: {Config.LOG_LEVEL}")
    print(f"DEVICE_PORT: {Config.DEVICE_PORT}")
    print(f"BAUD_RATE: {Config.BAUD_RATE}")
