import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        WIDTH = len(matrix)
        for h in range(math.ceil(WIDTH / 2)):
            for v in range(WIDTH // 2):
                tmp = matrix[WIDTH - 1 - v][h]
                matrix[WIDTH - 1 - v][h] = matrix[WIDTH - 1 - h][WIDTH - v - 1]
                matrix[WIDTH - 1 - h][WIDTH - v - 1] = matrix[v][WIDTH - 1 - h]
                matrix[v][WIDTH - 1 - h] = matrix[h][v]
                matrix[h][v] = tmp