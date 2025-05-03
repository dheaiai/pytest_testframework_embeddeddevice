# pytest_testframework_embeddeddevice
This is a flexible and scalable test automation framework built using Pytest for validating embedded and IoT devices. It supports testing over multiple communication interfaces such as MQTT, HTTP, Serial, SSH, and WebSocket. The framework is designed for automated functional, integration, and regression testing of IoT devices across domains like healthcare, automotive, smart home, and industrial IoT.

✅ Key Features
MQTT Client – Publish/subscribe message verification
HTTP Client – REST API testing (GET, POST, PUT, DELETE)
Serial Communication – Command-response validation over UART
SSH Client – Remote access and command execution
WebSocket Client – Real-time stream testing
Terminal Utility – Linux terminal interaction and scripting
Log Parsing & Conversion – Convert debug logs to CSV, extract KPIs and error codes
Thread & Time Utilities – Multi-threading support and timing helpers

📁 Folder Structure
lib/ – Core libraries for each protocol
utils/ – Reusable utilities: regex, timing, threading, KPI checks
config/ – Device and environment configuration files
tests/ – Pytest test scripts
convertDebugLogsToCsv/ – Debug log parser for CSV conversion
