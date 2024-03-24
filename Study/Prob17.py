from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = [""]
        for digit in digits:
            temp_combinations = []
            for combination in combinations:
                for char in num_dict[digit]:
                    temp_combinations.append(combination + char)
            combinations = temp_combinations

        return combinations