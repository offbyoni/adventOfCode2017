def generator(n, seed, factor):
    divisor = 2147483647
    previousResult = seed
    for i in range(0, n):
        previousResult *= factor
        previousResult %= divisor
        yield previousResult
