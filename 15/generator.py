class generator:
    factor = 16807
    previousResult = 65
    divisor = 2147483647

    def __init__(self):
        pass

    def generate(self):
        self.previousResult *= self.factor
        self.previousResult %= self.divisor
        return self.previousResult
