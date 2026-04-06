class QASMBuilder:
    def __init__(self, num_qubits=4):
        self.num_qubits = num_qubits
        self.qasm_lines = []
        self.initialise_qasm()

    def initialise_qasm(self):
        self.qasm_lines.append("OPENQASM 2.0;")
        self.qasm_lines.append('include "qelib1.inc";')
        self.qasm_lines.append(f"qreg q[{self.num_qubits}];")
        self.qasm_lines.append(f"creg c[{self.num_qubits}];")

    def add_hadamard(self, qubit):
        self.qasm_lines.append(f"h q[{qubit}];")

    def add_pauli_x(self, qubit):
        self.qasm_lines.append(f"x q[{qubit}];")

    def add_pauli_z(self, qubit):
        self.qasm_lines.append(f"z q[{qubit}];")

    def add_cnot(self, control, target):
        self.qasm_lines.append(f"cx q[{control}],q[{target}];")

    def add_measure_all(self):
        for i in range(self.num_qubits):
            self.qasm_lines.append(f"measure q[{i}] -> c[{i}];")

    def get_qasm(self):
        return "\n".join(self.qasm_lines)