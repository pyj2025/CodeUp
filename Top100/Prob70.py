class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        index_zero = 1
        index_one = 1
        
        result = 0
        
        for i in range(2, n+1):
            result = index_zero + index_one
            index_one = index_zero
            index_zero = result
        
        return result
