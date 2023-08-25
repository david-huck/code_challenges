
def isPalindromic(s):
    # s_len_half = 
    for i in range(int(len(s)/2)):
        if not s[i] == s[-(i+1)]:
            return False
    return True


if __name__=="__main__":
    test_cases = {
        "aba" : True,
        "abba" : True,
        "11" : True,
        "123" : False,

    }

    for case, result in test_cases.items():
        assert isPalindromic(case) == result

    upper_limit = 1000
    for i in range(upper_limit):
        for j in range(upper_limit):
            if isPalindromic(str(i*j)):
                print(i,j,i*j)
    pass
str.f