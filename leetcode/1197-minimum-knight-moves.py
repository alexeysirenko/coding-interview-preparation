from collections import deque

class Solution:
    def minKnightMoves(self, th: int, tv: int) -> int:
        possibleMoves = [
            [1, -2],
            [2, -1],
            [2, 1],
            [1, 2],
            [-1, 2],
            [-2, 1],
            [-2, -1],
            [-1, -2]
        ]

        visited = set()

        def traverse() -> int:
            H, V = 0, 1
            que = deque()
            que.append([0, 0])
            nSteps = 0
            while que:
                currLevelSize = len(que)
                for _ in range(currLevelSize):
                    curr = que.popleft()
                    if curr[H] == th and curr[V] == tv:
                        return nSteps
                    for move in possibleMoves:
                        newH = curr[H] + move[H]
                        newV = curr[V] + move[V]

                        if not (newH, newV) in visited:
                            que.append(  [ newH ,  newV ]  )
                            visited.add((newH, newV))


                nSteps += 1

        return traverse()



