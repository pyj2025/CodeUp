class Solution:
    def reverseWords(self, s: str) -> str:
        sList = s.split()
        res = []
        for i in sList:
            tmp = "".join(reversed(i))
            res.append(tmp)
        
        return " ".join(res)