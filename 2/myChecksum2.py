import re

class myChecksum2():

    def check(inString):
        lines = inString.split('\n')
        res = 0
        for line in lines:
            strings = re.split("\s", line)
            vals = list(map(int, strings))
            for idx, leftVal in enumerate(vals):
                for j in range(idx + 1, len(vals)):
                    rightVal = vals[j]
                    if leftVal % rightVal == 0:
                        res += leftVal / rightVal
                        break
                    if rightVal % leftVal == 0:
                        res += rightVal / leftVal
                        break
        return res
