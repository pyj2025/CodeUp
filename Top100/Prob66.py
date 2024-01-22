from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[n - 1] += 1
        
        carry = 0
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] %= 10
                carry = 1
            else:
                carry = 0
        
        if carry:
            digits.insert(0, 1)
        
        return digits