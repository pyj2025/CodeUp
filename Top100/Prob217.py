from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            numSet.add(num)

        if len(nums) == len(numSet):
            return False 
        else:
            return True