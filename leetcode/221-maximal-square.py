class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])

        # add an extra row and col of 0s so as not to check for index - 1 boundaries
        memo = [[0 for _ in range(width + 2)] for _ in range(height + 2)]

        maxLen = 0
        for row in range(height):
            for col in range(width):
                currLen = 0
                if matrix[row][col] == '1':
                    currLen = 1 + min(
                        memo[row - 1 + 1][col + 1],
                        memo[row + 1][col - 1 + 1],
                        memo[row - 1 + 1][col - 1 + 1]
                    )
                memo[row + 1][col + 1] = currLen
                maxLen = max(maxLen, currLen)

        return maxLen * maxLen