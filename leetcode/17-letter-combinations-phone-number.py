class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        maps = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        combinations = [[]]
        results = []
        for digit in digits:
            levelSize = len(combinations)
            for i in range(levelSize):
                result = combinations[i]
                for char in maps[digit]:
                    newResult = result[:]
                    newResult.append(char)
                    if len(newResult) == len(digits):
                        results.append(''.join(newResult))
                    else:
                        combinations.append(newResult)


        return results