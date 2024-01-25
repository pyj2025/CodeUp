class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        currIdx = 0
        for i in range(len(t)):
            if currIdx < len(s) and t[i] == s[currIdx]:
                currIdx += 1

        return currIdx == len(s)
                