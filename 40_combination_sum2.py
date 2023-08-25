from typing import Iterable
from copy import copy


class Solution:
    def combinationSum2(self, candidates, target: int) -> int:
        if not isinstance(candidates, Iterable):
            candidates = [candidates]

        candidates = sorted(candidates)

        if sum(candidates) < target:
            return []

        def combSum(candidates, target, temp_list, out, index):
            if target == 0:
                subs = sorted(copy(temp_list))
                if subs not in out:
                    out.append(subs)
                return out

            for i, _ in enumerate(candidates):
                if target - candidates[i] < 0:
                    return out
                temp_list.append(candidates[i])
                combSum(candidates[:i] + candidates[i+1:], target - candidates[i], temp_list, out, i)
                temp_list.pop()

            return out

        return combSum(candidates, target, [], [], 0)


if __name__ == "__main__":
    test_cases = {
        ((10, 1, 2, 7, 6, 1, 5), 8): [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
        ((2, 5, 2, 1, 2), 5): [[1, 2, 2], [5]],
        ((1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),27): []
    }

    for test, result in test_cases.items():
        c_result = Solution().combinationSum2(test[0], test[1])
        assert c_result == result
