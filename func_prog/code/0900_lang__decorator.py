"""
# Decorators
"""


class Pi:
    def __init__(self, precision=5):
        self._precision = precision

    @property
    def value(self):
        return format(3.141_592_653_589_793_238_46, f".{self._precision}f")

    @staticmethod
    def char():
        return "π"


print(Pi.char())
print(Pi(10).value)
