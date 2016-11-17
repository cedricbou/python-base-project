"""Demonstration classes"""
class Fiddlewith:
    """Demonstration class for test coverage"""

    def __init__(self):
        "defines the c operand"
        self.num_c = 32

    @staticmethod
    def add(num_a, num_b):
        "add a with b"
        return num_a + num_b

    def add_with_c(self, num_a, num_b):
        "add a with b and class member c"
        return num_a + num_b + self.num_c
