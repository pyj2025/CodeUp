from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        lo = self.binarySearch(nums, target, True)
        hi = self.binarySearch(nums, target, False)
        
        return [lo, hi]
        
    def binarySearch(self, nums, target, isLeft):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                if isLeft:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        
        if isLeft:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                return -1    
        else:
            if nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            else:
                return -1


    
        