class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1