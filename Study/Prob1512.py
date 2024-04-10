from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_dict = dict()
        res = 0

        for i in nums:
            if i not in num_dict:
                num_dict[i] = 0
            num_dict[i] += 1
            res += num_dict[i] - 1

        return res