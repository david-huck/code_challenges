from typing import Iterable
from copy import copy

class Solution:
    def combinationSum(self, candidates, target: int) -> int:
        if not isinstance(candidates, Iterable):
            candidates = [candidates]
        combinations = []

        candidates = sorted(candidates)

        def combSum(candidates, target, temp_list, out, index):
            if target == 0:
                subs = sorted(copy(temp_list))
                if subs not in out:
                    out.append(subs)
                return out
            
            for i,_ in enumerate(candidates):
                if target - candidates[i] < 0:
                    return out
                temp_list.append(candidates[i])
                combSum(candidates, target - candidates[i], temp_list, out, i)
                temp_list.pop()

            return out
        
        return combSum(candidates, target, [], [], 0)

        # def recursive_remainder(candidates, target, old_target, i=0, initial_i=0):
        #     if i - initial_i >= len(candidates):
        #         return []
            

        #     c = candidates[i%len(candidates)]

        #     if target - c == 0:
        #         return [c]
        #     # elif target - c in candidates:
        #     #     idx_of_final_piece = candidates.index(target - c)
        #     #     return [c] + recursive_remainder(candidates, target - c, old_target, idx_of_final_piece)
        #     elif target - c  < min(candidates):
        #         return recursive_remainder(candidates, target, old_target, i+1, initial_i=initial_i)
        #     else:
        #         rrem = recursive_remainder(candidates, target- c, old_target, i, initial_i=initial_i)
        #         if rrem == []:
        #             return []
        #         return [c] + rrem

        # for i in range(len(candidates)):
        #     rrem =  recursive_remainder(candidates, target, target,i, initial_i=i)
        #     if rrem != [] and sorted(rrem) not in combinations:
        #         combinations.append(sorted(rrem))

        return combinations

        # p1, p2 = 0, len(candidates)-1
        
        # while remainder > 0:
        #     if remainder - candidates[p2] < 0:
        #         p2 -= 1
        #     else:
        #         remainder -= candidates[p2]
        #         combinations.append(candidates[p2])
            
        #     if remainder - candidates[p1] < 0:
        #         return combinations
        #     else:
        #         remainder -= candidates[p1]
        #         combinations.append(candidates[p1])
            



if __name__ == "__main__":
    test_cases = {
        ((2, 3, 6, 7), 7): [[2, 2, 3], [7]],
        ((2,3,5),8): [[2,2,2,2],[2,3,3],[3,5]],
        ((2),1): [],
        ((7,3,2),18):[[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
        }

    for test, result in test_cases.items():
        c_result = Solution().combinationSum(test[0], test[1])
        assert c_result == result
