from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)

        for i in range(0, len(indices)):
            res[indices[i]] = s[i]

        return "".join(res)