from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
    
        max_num = nums[0]
        min_num = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            tmp = max(nums[i], max_num * nums[i], min_num * nums[i])
            min_num = min(nums[i], max_num * nums[i], min_num * nums[i])
            max_num = tmp
            result = max(max_num, result)

        return result

