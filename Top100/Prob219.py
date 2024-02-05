from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = defaultdict()
        
        for i in range(0, len(nums)):
            if nums[i] in numSet and abs(i - numSet[nums[i]]) <= k:
                return True
            else:
                numSet[nums[i]] = i 

        return False