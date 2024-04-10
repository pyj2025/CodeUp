from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        sortedNums = sorted(nums_set)

        maxLength = 1
        currentLength = 1

        for i in range(1, len(sortedNums)):
            if sortedNums[i] != sortedNums[i - 1]:
                if sortedNums[i] == sortedNums[i - 1] + 1:
                    currentLength += 1
                else:
                    currentLength = 1
                maxLength = max(maxLength, currentLength)

        return maxLength
