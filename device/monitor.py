import serial
from core.port import detect_esp32


def start_monitor():
    port = detect_esp32()

    if not port:
        return

    try:
        ser = serial.Serial(port, 115200, timeout=1)
        print("📡 Serial Monitor Started (Press Ctrl+C to stop)\n")

        while True:
            line = ser.readline().decode(errors="ignore").strip()
            if line:
                print(f"ESP32 → {line}")

    except KeyboardInterrupt:
        print("\n🛑 Serial monitor stopped")