from ai.generator import generate_code, clean_code
from core.project import create_project, save_code
from core.executor import compile_code, upload_code
from device.monitor import start_monitor
import time



def main():
    user_command = input("Enter your command: ")

    create_project()

    print("🤖 Generating code...")
    code = generate_code(user_command)
    save_code(code)

    print("⚙️ Compiling...")
    result = compile_code()

    max_attempts = 3
    attempt = 0

    while result.returncode != 0 and attempt < max_attempts:
        if "error" not in result.stderr.lower():
            break

        print(f"🔧 Fixing error... Attempt {attempt + 1}")

        time.sleep(4)  # ✅ prevent API rate limit

        code = clean_code(code)
        save_code(code)

        result = compile_code()
        attempt += 1

    if result.returncode != 0:
        print("❌ Failed after 3 attempts")
        print(result.stderr)
        return

    print("🚀 Uploading...")
    upload_code()

    print("✅ Done!")

    


if __name__ == "__main__":
    main()

print("📡 Starting Serial Monitor...")
start_monitor()