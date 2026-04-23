from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from threading import Thread
import serial
import time

from core.port import detect_esp32
from ai.generator import generate_code
from core.project import create_project, save_code
from core.executor import compile_code, upload_code

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# 🔥 GLOBAL SERIAL INSTANCE
ser = None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run():
    global ser

    command = request.json.get("command")
    logs = []

    try:
        create_project()
        logs.append("📁 Project ready")

        code = generate_code(command)
        save_code(code)
        logs.append("💾 Code generated")

        result = compile_code()

        if result.returncode != 0:
            logs.append("❌ Compile error")
            logs.append(result.stderr)
            return jsonify({"logs": logs, "status": "error"})

        # 🔥 CLOSE SERIAL BEFORE UPLOAD
        close_serial()

        upload_code()
        logs.append("🚀 Uploaded")

        # 🔥 START SERIAL STREAM SAFELY
        Thread(target=serial_stream, daemon=True).start()

        return jsonify({"logs": logs, "code": code})

    except Exception as e:
        return jsonify({"logs": [str(e)]})


# 🔌 SAFE CLOSE SERIAL
def close_serial():
    global ser
    if ser and ser.is_open:
        try:
            ser.close()
            print("🔌 Serial closed")
        except:
            pass


# 📡 SERIAL STREAM (IMPROVED)
def serial_stream():
    global ser

    port = detect_esp32()
    if not port:
        print("❌ No port found")
        return

    # 🔥 WAIT FOR PORT RELEASE AFTER UPLOAD
    time.sleep(2)

    # 🔥 RETRY OPENING PORT
    for i in range(5):
        try:
            ser = serial.Serial(port, 115200, timeout=1)
            print("📡 Serial connected")
            break
        except Exception as e:
            print(f"Retry {i+1}: {e}")
            time.sleep(1)

    if not ser:
        print("❌ Failed to open serial")
        return

    # 🔁 READ LOOP
    while True:
        try:
            line = ser.readline().decode(errors="ignore").strip()
            if line:
                socketio.emit("serial", {"data": line})
        except Exception as e:
            print("Serial error:", e)
            break


if __name__ == "__main__":
    socketio.run(app, debug=True)