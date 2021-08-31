from collections import deque

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        que = [[]]
        results = []
        for num in range(1, n + 1):
            levelSize = len(que)
            for currIdx in range(levelSize):
                currComb = que[currIdx]
                newComb = currComb[:]
                newComb.append(num)
                if len(newComb) == k:
                    results.append(newComb)
                else:
                    que.append(newComb)

        return results


