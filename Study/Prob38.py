class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(0, n-1):
            prev, tmp, count = s[0], '', 0
            
            for c in s:
                if prev == c:
                    count += 1
                else:
                    tmp += str(count) + prev
                    prev = c
                    count = 1
            
            tmp += str(count) + prev
            s = tmp
            
        return s