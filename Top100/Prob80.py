from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2] or nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        
        return k