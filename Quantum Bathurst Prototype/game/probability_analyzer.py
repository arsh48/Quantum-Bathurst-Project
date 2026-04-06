class ProbabilityAnalyzer:
    def __init__(self, quantum_system):
        self.quantum_system = quantum_system

    def get_probabilities(self):
        state = self.quantum_system.get_statevector()
        return state.probabilities_dict()

    def crash_probability(self):
        probs = self.get_probabilities()
        crash_states = ['1111', '1110', '1101']
        crash_prob = 0

        for state, prob in probs.items():
            if state in crash_states:
                crash_prob += prob

        return crash_prob