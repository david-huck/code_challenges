from itertools import permutations

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set(s)

        if len(s) == len(unique_chars):
            return len(s)
        
        substr_lens = []
        for i in range(len(s)):
            substr_len = 1
            while i+substr_len < len(s):
                if s[i+substr_len] not in s[i:i+substr_len]:
                    substr_len += 1
                else:
                    break
            substr_lens.append(substr_len)

        return max(substr_lens)
        # longest_len = 0
        # for i in range(len(unique_chars), 0, -1):
        #     perms = permutations(unique_chars, i)
        #     for p in perms:
        #         substr = "".join(p)
        #         if s.find(substr) >= 0:
        #             longest_len = max(longest_len, len(substr))
        #             if longest_len==len(unique_chars):
        #                 return longest_len
        # return longest_len

        # longest_dist = 0
        # for char in s:
        #     start = s.find(char)
        #     while start != -1:
        #         next_occ = s.find(char,start+1)
        #         if next_occ == -1:
        #             c_dist = len(s) - start
        #         else:
        #             c_dist = next_occ - start
        #         if c_dist > longest_dist:
        #             longest_dist = c_dist
        #         start = next_occ
        # return longest_dist
        

if __name__ == "__main__":
    test_cases = {
        "nfvbiywbasfbu": 7,  
        "abcabcd" : 4,
        "abcabcbb" : 3,
        "bbbbb" : 1,
        "pwwkew" : 3,
        " ": 1,
        "a": 1, 
        "au": 2, 
        "aab": 2,  
          }

    for test, result in test_cases.items():
        assert Solution().lengthOfLongestSubstring(test) == result