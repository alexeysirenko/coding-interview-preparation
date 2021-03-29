class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def traverse(leftIdx, rightIdx):
            if leftIdx >= rightIdx:
                return 1
            len = rightIdx - leftIdx + 1
            if len in memo:
                return memo[len]

            sum = 0
            for rootIdx in range(leftIdx, rightIdx + 1):
                nTreesLeft = traverse(leftIdx, rootIdx - 1)
                nTreesRight = traverse(rootIdx + 1, rightIdx)
                sum += nTreesLeft * nTreesRight

            memo[len] = sum

            return sum

        return traverse(0, n - 1)