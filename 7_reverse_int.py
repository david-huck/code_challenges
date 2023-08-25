class Solution:
    def reverse(self, x: int) -> int:
        str_int = str(x)
        negative = str_int[0] == "-"
        if negative:
            sign=-1
            num = int(str(x)[:0:-1])
        else:
            sign=1
            num = int(str(x)[::-1])
        try:
            result = sign*num
        except:
            result = 0
        return result

if __name__ == "__main__":
    test_cases = {
         123: 321,
         -123: -321,
         120: 21,
         1534236469: 0
         
    }

    for test, result in test_cases.items():
        c_result = Solution().reverse(test)
        assert c_result == result