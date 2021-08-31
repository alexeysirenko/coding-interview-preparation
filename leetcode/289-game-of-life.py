class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        DEAD, ALIVE, DEAD_TO_DEAD, DEAD_TO_ALIVE, ALIVE_TO_DEAD, ALIVE_TO_ALIVE = 0, 1, 2, 3, 4, 5
        PREV_ALIVE_STATES = set([ALIVE, ALIVE_TO_DEAD, ALIVE_TO_ALIVE])
        CURR_ALIVE_STATES = set([ALIVE, DEAD_TO_ALIVE, ALIVE_TO_ALIVE])
        height = len(board)
        width = len(board[0])
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

        def isCellAlive(v, h):
            if v < 0 or v >= height or h < 0 or h >= width:
                return False
            else:
                return board[v][h] in PREV_ALIVE_STATES

        def nAliveAround(v, h):
            nAlive = 0
            for nv, nh in neighbors:
                if isCellAlive(v + nv, h + nh):
                    nAlive += 1
            return nAlive

        for v in range(height):
            for h in range(width):
                nAlive = nAliveAround(v, h)
                needsToDie = nAlive < 2 or nAlive > 3
                keepsLiving = nAlive == 2 or nAlive == 3
                becomesAliveIfDead = nAlive == 3
                currCell = board[v][h]
                if currCell == DEAD:
                    if becomesAliveIfDead:
                        board[v][h] = DEAD_TO_ALIVE
                    else:
                        board[v][h] = DEAD_TO_DEAD
                else:
                    if needsToDie:
                        board[v][h] = ALIVE_TO_DEAD
                    else:
                        board[v][h] = ALIVE_TO_ALIVE

        for v in range(height):
            for h in range(width):
                if board[v][h] in CURR_ALIVE_STATES:
                    board[v][h] = ALIVE
                else:
                    board[v][h] = DEAD
