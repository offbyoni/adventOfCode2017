class myChecksum():

    def check(inString):
        lines = inString.split('\n')
        res = 0
        for line in lines:
            strings = line.split("\t")
            l = list(map(int, strings))
            maxVal = max(l)
            minVal = min(l)
            lineCheck = maxVal - minVal
            res += lineCheck
        return res
