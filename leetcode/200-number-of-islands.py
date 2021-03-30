class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        def isLand(h, w):
            return h >= 0 and w >= 0 and h < height and w < width and grid[h][w] != "0"

        def dfs(h, w):
            if not isLand(h, w):
                return
            grid[h][w] = "0"
            dfs(h - 1, w)
            dfs(h, w - 1)
            dfs(h + 1, w)
            dfs(h, w + 1)


        numIslands = 0
        for h in range(height):
            for w in range(width):
                if isLand(h, w):
                    numIslands += 1
                    dfs(h, w)

        return numIslands
