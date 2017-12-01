class captcha():
    def capt(in_string):
        res = 0
        for index, obj in enumerate(in_string):
            if index < len(in_string) - 1:
                next_ = in_string[index + 1]
            else:
                next_ = in_string[0]
            if obj == next_:
                res += int(obj)
        return res
