from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
    
        size = len(nums)
        results = list()

        start = nums[0]
        end = nums[0]

        for i in range(1, size):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    results.append(str(start))
                else:
                    results.append(f"{start}->{end}")

                start = nums[i]
                end = nums[i]
        
        if start == end:
            results.append(str(start))
        else:
            results.append(f"{start}->{end}")
        
        return results
