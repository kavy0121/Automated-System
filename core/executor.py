import subprocess
from config import PROJECT_PATH
from core.port import detect_esp32


def run_cmd(cmd):
    return subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        cwd=PROJECT_PATH   # ✅ FIXED
    )


def compile_code():
    return run_cmd("pio run")


def upload_code():
    port = detect_esp32()

    if not port:
        print("❌ Cannot upload (no device)")
        return

    return run_cmd(f"pio run --target upload --upload-port {port}")