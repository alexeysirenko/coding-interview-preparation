class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def removeIsland(v, h):
            if v < 0 or h < 0 or v >= len(grid) or h >= len(grid[v]) or grid[v][h] != 0:
                return
            grid[v][h] = 1
            removeIsland(v, h + 1)
            removeIsland(v + 1, h)
            removeIsland(v - 1, h)
            removeIsland(v, h - 1)

        def excludeUnclosedIslands():
            for v in [0, len(grid) - 1]:
                for h in range(len(grid[v])):
                    removeIsland(v, h)

            for v in range(len(grid)):
                for h in [0, len(grid[v]) - 1]:
                    removeIsland(v, h)

        def countIslands() -> int:
            nIslands = 0
            for v in range(len(grid)):
                for h in range(len(grid[v])):
                    if grid[v][h] == 0:
                        nIslands += 1
                        removeIsland(v, h)
            return nIslands

        excludeUnclosedIslands()
        #print(grid)
        return countIslands()