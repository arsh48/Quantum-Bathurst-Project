import random

class NoiseModel:
    def __init__(self):
        self.noise_level = 0

    def increase_noise(self):
        self.noise_level += 1

    def get_noise_qubit(self):
        return random.randint(0, 3)

    def should_apply_noise(self):
        return random.random() < (0.2 + self.noise_level * 0.05)