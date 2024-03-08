from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        sums = (mean * (m + n)) - sum(rolls)

        if sums < n or sums > (n * 6):
            return []
        else:
            res = []

            while sums > 0:
                dice = min(sums - n + 1, 6)
                res.append(dice)
                sums -= dice
                n -= 1

            return res