class Solution:
    def myAtoi(self, s: str) -> int:
        new_str = s.strip()

        if not new_str:
            return 0
        
        idx = 0
        sign = "+"
        if new_str[0] in ["+", "-"]:
            sign = new_str[idx]
            idx += 1

        digits = ""
        while idx < len(new_str) and new_str[idx] in ["0","1","2","3","4","5","6","7","8","9"]:
            digits += new_str[idx]
            idx += 1
        
        if not digits:
            return 0
        
        res = int(digits)
        

        if sign == "-":
            res = -res
        
        smallest, biggest = -2**31, 2**31 - 1

        if res > biggest:
            return biggest
        elif res < smallest:
            return smallest
        else:
            return res