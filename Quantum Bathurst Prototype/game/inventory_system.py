class InventorySystem:
    def __init__(self):
        self.gates = {
            "H": 5,
            "X": 4,
            "Z": 4,
            "CNOT": 3
        }

    def use_gate(self, gate):
        if self.gates.get(gate, 0) > 0:
            self.gates[gate] -= 1
            return True
        return False

    def get_inventory(self):
        return self.gates