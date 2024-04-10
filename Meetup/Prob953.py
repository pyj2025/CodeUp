class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(0, len(order)):
            dic[order[i]] = i
        
        prev = []
        for ch in words[0]:
            prev.append(dic[ch])
        
        for i in range(1, len(words)):
            cur = []
            for ch in words[i]:
                cur.append(dic[ch])
            
            if cur < prev:
                return False
            
            prev = cur
            
        return True