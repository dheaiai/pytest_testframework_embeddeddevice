
# Embedded Device Test Framework (Pytest-Based)

This repository provides a robust and extensible test framework built using `pytest` to test embedded devices via various protocols (MQTT, HTTP, Serial, SSH, WebSocket).

---

## 📦 Folder Structure

```
embedded_test_framework/
├── conftest.py                # Pytest fixtures
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Python dependencies
├── config/                    # Device and global configuration files
├── converters/                # Log conversion tools
├── dataset/                   # Input/output test data
├── lib/                       # Protocol client/server libraries
├── scripts/                   # Optional helper scripts
├── tests/                     # Pytest test cases
└── utils/                     # Utility functions (terminal, regex, threading, etc.)
```

---

## ✅ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests

```bash
pytest
```

You can run individual tests:

```bash
pytest tests/test_device_config.py
```

---

## ⚙️ Configuration

Edit `config/config_dev1.json` and `config/common_settings.yaml` to match your embedded device setup.

---

## 🔌 Supported Protocols

- **MQTT** — `lib/mqtt_client.py`
- **HTTP** — `lib/http_server.py`
- **Serial** — `lib/serial_comm.py`
- **SSH** — `lib/ssh_client.py`
- **WebSocket** — `lib/websocket_client.py`

---

## 🛠 Utilities

- **Terminal commands**: `utils/terminal_util.py`
- **Regex operations**: `utils/regex_util.py`
- **Path management**: `utils/path_util.py`
- **Threading**: `utils/thread_util.py`
- **Timing**: `utils/time_util.py`
- **KPI calculation**: `utils/kpi_util.py`

---

## 📄 Sample Tests

- `test_device_config.py` — Ping device based on config
- `test_logs_conversion.py` — Convert raw logs to CSV format

---

## 📁 Log Conversion

Log files can be converted using `converters/debug_logs_to_csv.py` to simplify analysis.

---

## 📌 Notes

- Make sure devices are connected and network-accessible.
- Update serial/SSH credentials in the config files.
- Use `pytest -s` to see real-time terminal output.

---

## 📬 Contributions

Feel free to extend this framework with more tests, protocol support, or utilities. PRs are welcome!

