class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sMap = {}
        for ch in s:
            sMap[ch] = sMap.get(ch, 0) + 1
        
        result = ''
        for ch in order:
            if ch in sMap and sMap[ch] > 0:
                result += sMap[ch] * ch
                

        for key, val in sMap.items():
            if val > 0 and key not in result:
                result += val * key
        
        return result      