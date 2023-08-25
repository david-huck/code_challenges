class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }

        open_brs = []
        for i,br in enumerate(s):
            if br in matching_brackets.keys():
                open_brs.append(br)
            elif br in matching_brackets.values():
                if br == matching_brackets[open_brs[-1]]:
                    open_brs.pop()
                else:
                    return False
                
        return len(open_brs)==0

            #j = find_closing_br(br,s[i+1:])

if __name__ == "__main__":
    test_cases = {
        "()" : True,
        r"()[]{}" : True,
        "(]" : False,
        "(())" : True,
        "(([)])" : False,
        r"{()[]([]{})}": True
        }

    for test, result in test_cases.items():
        assert Solution().isValid(test) == result