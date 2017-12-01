class captcha():
    def capt(input):
        in_string = str(input)
        res = 0
        for index, obj in enumerate(in_string):
            if index < len(in_string) - 1:
                next_ = in_string[index + 1]
            else:
                next_ = in_string[0]
            if obj == next_:
                res += int(obj)
        return res
