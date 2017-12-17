def generator(n, seed, factor):
    genInt = generatorInt(seed, factor)
    for i in range(0, n):
        yield next(genInt)

def generatorInt(seed, factor):
    divisor = 2147483647
    previousResult = seed
    while True:
        previousResult *= factor
        previousResult %= divisor
        yield previousResult

def generatorMod(n, seed, factor, modulo):
    genInt = generatorInt(seed, factor)
    i = 0
    while i < n:
        nextNumber = next(genInt)
        if nextNumber % modulo == 0:
            i += 1
            yield(nextNumber)
