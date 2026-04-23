import ollama


# ✅ Clean AI output properly
def clean_code(text):
    # Remove markdown
    text = text.replace("```cpp", "").replace("```", "")

    # Keep only code starting from #include
    if "#include" in text:
        text = text[text.index("#include"):]

    return text.strip()


# ✅ Fallback if AI fails
def fallback_code(command):
    return """
#include <Arduino.h>

void setup() {
  pinMode(2, OUTPUT);
}

void loop() {
  digitalWrite(2, HIGH);
  delay(1000);
  digitalWrite(2, LOW);
  delay(1000);
}
"""


# ✅ Generate code
def generate_code(user_command):
    prompt = f"""
You are a professional embedded systems engineer.

Generate ONLY valid ESP32 Arduino C++ code.

Instruction:
{user_command}

STRICT RULES:
- Output ONLY C++ code
- NO explanation
- NO markdown (no ``` )
- Code must start with #include
- Must compile in PlatformIO
"""

    try:
        print("🧠 Sending request to Ollama...")

        response = ollama.chat(
            model="llama3",   # 🔥 use this (faster & stable)
            messages=[{"role": "user", "content": prompt}]
        )

        code = clean_code(response['message']['content'])

        # ✅ Safety check
        if "#include" not in code:
            print("❌ Invalid AI output, using fallback")
            return fallback_code(user_command)

        print("✅ Code generated")
        return code

    except Exception as e:
        print("❌ Ollama error:", e)
        return fallback_code(user_command)


# ✅ Fix code
def fix_code(code, error):
    prompt = f"""
You are an expert embedded systems debugger.

Fix this ESP32 Arduino code.

Code:
{code}

Error:
{error}

STRICT RULES:
- Output ONLY corrected C++ code
- NO explanation
- NO markdown
- Code must start with #include
- Must compile without errors
"""

    try:
        print("🛠 Fixing code using AI...")

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        fixed = clean_code(response['message']['content'])

        # ✅ Safety check
        if "#include" not in fixed:
            print("❌ Fix failed, keeping old code")
            return code

        return fixed

    except Exception as e:
        print("❌ Fix error:", e)
        return code