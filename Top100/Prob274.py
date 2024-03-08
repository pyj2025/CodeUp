from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sortedArr = sorted(citations)
        size = len(sortedArr)
        
        for i in range(0, size):
            if sortedArr[i] >= (size - i):
                return size - i

        return 0