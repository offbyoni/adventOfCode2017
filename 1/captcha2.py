class captcha2():
    def capt2(in_string):
        res = 0
        for index, obj in enumerate(in_string):
            offset = len(in_string) / 2
            pairIndex = (index + int(offset)) % len(in_string)
            pair = in_string[pairIndex]
            if obj == pair:
                res += int(obj)
        return res
