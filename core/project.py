import os
import subprocess
from config import PROJECT_PATH


def create_project():
    # ✅ Create folder if missing
    if not os.path.exists(PROJECT_PATH):
        os.makedirs(PROJECT_PATH)

    # ✅ Check if already initialized
    ini_path = os.path.join(PROJECT_PATH, "platformio.ini")

    if not os.path.exists(ini_path):
        print("📁 Initializing PlatformIO project...")
        subprocess.run(
            f"pio project init --board esp32dev",
            shell=True,
            cwd=PROJECT_PATH   # ✅ VERY IMPORTANT FIX
        )


def save_code(code):
    src_path = os.path.join(PROJECT_PATH, "src")
    os.makedirs(src_path, exist_ok=True)

    file_path = os.path.join(src_path, "main.cpp")

    with open(file_path, "w") as f:
        f.write(code)

    print("💾 Code saved")