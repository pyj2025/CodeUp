import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = collections.Counter(ransomNote)
        magazine_freq = collections.Counter(magazine)

        for char, count in ransom_freq.items():
            if magazine_freq[char] < count:
                return False

        return True

