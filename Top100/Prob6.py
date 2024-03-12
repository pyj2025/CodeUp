class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        
        idx = 0
        step = -1
        for char in s:
            rows[idx].append(char)
            if idx == 0:
                step = 1
            if idx == numRows - 1:
                step = -1
            
            idx += step

        for i in range(0, numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)