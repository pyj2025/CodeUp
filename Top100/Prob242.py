import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = collections.Counter(s)
        t_freq = collections.Counter(t)

        for char, count in s_freq.items():
            if t_freq[char] < count:
                return False

        return True