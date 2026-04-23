import serial.tools.list_ports


def detect_esp32():
    ports = serial.tools.list_ports.comports()

    for port in ports:
        desc = port.description.lower()

        if any(x in desc for x in ["cp210", "ch340", "usb", "uart"]):
            print(f"🔌 ESP32 detected on {port.device}")
            return port.device

    print("❌ No ESP32 found")
    return None