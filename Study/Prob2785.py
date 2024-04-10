class Solution:
    def sortVowels(self, s: str) -> str:
        VOWELS = ["A","E","I","O","U","a","e","i","o","u"]
        vowel_idx = []

        for i in s:
            if i in VOWELS:
                vowel_idx.append(i)
            
        vowel_idx.sort()
        
        idx = 0
        word = ""
        for i in range(len(s)):
            if s[i] in VOWELS:
                word += vowel_idx[idx]
                idx += 1 
            else:
                word += s[i]

        return word