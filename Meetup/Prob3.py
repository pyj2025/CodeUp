class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        right = 0
        longest = 0

        while right < len(s):
            if s[right] not in charSet:
                charSet.add(s[right])
                longest = max(longest, len(charSet))
                right += 1
            else:
                charSet.remove(s[left])
                left += 1

        return longest