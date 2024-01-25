class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        reversed_words = reversed(words)
        reversed_string = ' '.join(reversed_words)

        return reversed_string