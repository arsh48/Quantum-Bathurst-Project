from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from game.qasm_builder import QASMBuilder

class QuantumSystem:
    def __init__(self):
        self.qc = QuantumCircuit(4, 4)
        self.qasm = QASMBuilder(4)
        self.initialise()

    def initialise(self):
        # Entangle driver and car reliability
        self.qc.h(0)
        self.qc.cx(0, 1)

        self.qasm.add_hadamard(0)
        self.qasm.add_cnot(0, 1)

    def aggressive_drive(self):
        self.qc.h(0)
        self.qc.x(2)

        self.qasm.add_hadamard(0)
        self.qasm.add_pauli_x(2)

    def safe_drive(self):
        self.qc.z(0)
        self.qasm.add_pauli_z(0)

    def pit_stop(self):
        self.qc.x(1)
        self.qc.z(1)

        self.qasm.add_pauli_x(1)
        self.qasm.add_pauli_z(1)

    def strategy_change(self):
        self.qc.h(2)
        self.qasm.add_hadamard(2)

    def add_noise(self, qubit):
        self.qc.z(qubit)
        self.qasm.add_pauli_z(qubit)

    def get_statevector(self):
        return Statevector.from_instruction(self.qc)

    def measure_all(self):
        self.qc.measure(range(4), range(4))
        self.qasm.add_measure_all()

    def get_qasm(self):
        return self.qasm.get_qasm()