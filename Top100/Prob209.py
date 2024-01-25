from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        min_len = float('inf')
        current_sum = 0

        while right < len(nums):
            current_sum += nums[right]
            right += 1

            while current_sum >= target:
                min_len = min(min_len, right - left)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len