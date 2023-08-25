# "PAYPALISHIRING", 5
# P       H
# A     S I
# Y   I   R
# P L     I
# A       G

# 1st row indices: 0, 8
# 2nd row indices: 1, 7,  9 
# 3rd row indices: 2, 6, 10
# 4th row indices: 3, 5, 11
# 5th row indices: 4,12


# "SOMEOTHERLONGERSTRING", 6
# S      O     G
# O    L N    N
# M   R  G   I
# E  E   E  R
# O H    R T
# T      S

# 1st row indices: 0, 10, 20
# 2nd row indices: 1, 9, 11, 18
# 3rd row indices: 2, 8, 
# 4th row indices: 3, 7,
# 5th row indices: 4, 6,
# 6th row indices: 5, 15
class Solution:
    def convert(self, s, numRows):
        rows = ["" for _ in range(numRows)]
#        s_i = 0
        i = 0
        sign = 1
        s = list(s)
        while s:
            rows[i] += s.pop(0)
            if i + sign == numRows or i + sign < 0:
                sign *= -1
            i += sign
        
        return "".join(rows)

if __name__ == "__main__":
    test_cases = {
         ("PAYPALISHIRING", 3): "PAHNAPLSIIGYIR",
         ("PAYPALISHIRING", 4): "PINALSIGYAHRPI",
        #  -123: -321,
        #  120: 21,
        #  1534236469: 0
         
    }

    for test, result in test_cases.items():
        c_result = Solution().convert(test[0], test[1])
        assert c_result == result