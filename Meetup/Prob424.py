import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        
        max_freq = 0 
        curr = 0
        result = 0
        d = collections.defaultdict(int)

        for right in range(0, len(s)):
            d[s[right]] += 1
            max_freq = max(max_freq, d[s[right]])
            
            if right - curr - max_freq >= k:
                d[s[curr]] -= 1
                curr += 1

            result = right + 1 - curr 
        
        return result