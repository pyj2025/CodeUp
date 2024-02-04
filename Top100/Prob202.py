class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 10:
            if n == 1 or n == 7:
                return True
            else:
                return False

        total = 0
        while n > 0:
            sq = n % 10
            total += sq ** 2
            n -= sq
            n /= 10
        
        if total == 1:
            return True

        return self.isHappy(total)