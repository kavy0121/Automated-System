class PinMapper:
    def __init__(self):
        self.map = {
            "PIN_2": "a1",
            "PIN_3": "b1",
            "VCC": "rail_vcc",
            "GND": "rail_gnd"
        }

    def get_node(self, pin):
        return self.map.get(pin)