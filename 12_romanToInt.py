class Solution:
    symbol_map = {
        "I":  1,
        "V":  5,  
        "X":  10, 
        "L":  50, 
        "C":  100,    
        "D":  500,    
        "M":  1000,   
    }
    subtractions = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    def romanToInt(self, s: str) -> int:
        # extract subtraction cases
        # for roman, i in self.subtractions.items(): 
        #     s = s.replace(roman, i)
        
        # for char in s:

        summands = []
        skip_i = None
        for i, char in enumerate(s):
            if i == skip_i:
                continue
            
            if i + 1 < len(s):
                potential_sub = s[i:i+2]
                if potential_sub in self.subtractions.keys():
                    summands.append(self.subtractions[potential_sub])
                    skip_i = i+1
                    continue

            summands.append(self.symbol_map[char])

        return sum(summands)            


if __name__ == "__main__":
    test_cases = {
        "XIV" : 14,
        "III" : 3,
        "LVIII" : 58,
        "MCMXCIV" : 1994,
    }

    for test, result in test_cases.items():
        assert Solution().romanToInt(test) == result
