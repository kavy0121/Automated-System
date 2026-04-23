def plan_circuit(command):
    # simple rule-based for now
    if "led" in command.lower():
        return {
            "components": ["LED", "RESISTOR"],
            "chain": ["PIN_2", "LED", "RESISTOR", "GND"]
        }

    return None