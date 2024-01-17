from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sortedArr = nums
        sortedArr.sort()
        
        for i in range(len(sortedArr)):
            if i != sortedArr[i]:
                return i
        
        return len(sortedArr)