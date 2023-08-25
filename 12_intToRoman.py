class Solution:
    symbol_map = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M",
    }
    def int_to_roman(self, num: int) -> str:
        roman_int = ""
        roman_values = list(self.symbol_map.keys())
        smaller_roman_val = 0
        while num > 0:
            # find largest roman closest to but smaller num 
            for i,v in enumerate(roman_values):
                smaller_roman_val = v
                if i < len(roman_values)-1:
                    if roman_values[i+1] > num:
                        break

            # subtract that roman, and add it to roman_int
            num -= smaller_roman_val
            roman_int += self.symbol_map[smaller_roman_val]
            # repeat with the remainder

        return roman_int

if __name__ == "__main__":
    test_cases = {
        14 : "XIV",
        3 : "III",
        58 : "LVIII",
        1994 : "MCMXCIV",
    }

    for test, result in test_cases.items():
        assert Solution().int_to_roman(test) == result
