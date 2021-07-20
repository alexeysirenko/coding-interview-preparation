class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        charIdx = 0
        memo = {}
        def traverse(charIdx: int):
            if charIdx in memo:
                return memo[charIdx]
            if charIdx >= len(s):
                memo[charIdx] = True
                return True
            for endIdx in range(charIdx, len(s) + 1):
                if s[charIdx:endIdx] in wordSet:
                    if traverse(endIdx):
                        memo[charIdx] = True
                        return True

            memo[charIdx] = False
            return False

        return traverse(0)


