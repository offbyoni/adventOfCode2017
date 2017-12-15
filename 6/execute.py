from reallocate import reallocationCount, reallocationLoopSize

banks = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
res = reallocationCount(banks)
print(res)
res = reallocationLoopSize(banks)
print(res)
