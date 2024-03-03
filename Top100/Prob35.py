from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        
        for i in range (0, l):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        
        return l