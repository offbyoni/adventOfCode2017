def judge(genA, genB):
    pairs = zip(genA, genB)
    sum = 0
    for pair in pairs:
        lowest16A = pair[0] % 65536
        lowest16B = pair[1] % 65536
        if lowest16A == lowest16B:
            sum += 1
    return sum
