class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def traverse(v, h) -> int:
            if v < 0 or h < 0 or v >= len(grid) or h >= len(grid[v]):
                return 0
            elif grid[v][h] == 0:
                return 0
            else:
                grid[v][h] = 0
                return 1 + traverse(v + 1, h) + traverse(v, h + 1) + traverse(v - 1, h) + traverse(v, h - 1)

        maxArea = 0
        for v in range(len(grid)):
            for h in range(len(grid[v])):
                maxArea = max(maxArea, traverse(v, h))

        return maxArea