from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0
        count = 0
        last = 0

        for i in range(0, len(nums) - 1):
            curr = max(curr, i + nums[i])

            if i == last:
                last = curr
                count += 1
        
        return count