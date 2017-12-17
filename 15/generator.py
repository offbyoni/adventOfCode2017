class generator:
    divisor = 2147483647

    def __init__(self, seed, factor):
        self.factor = factor
        self.previousResult = seed

    def generate(self):
        self.previousResult *= self.factor
        self.previousResult %= self.divisor
        return self.previousResult
