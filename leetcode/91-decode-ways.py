class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def traverse(idx):
            if idx in memo:
                return memo[idx]

            if idx < len(s) and s[idx] == '0':
                return 0
            if idx >= len(s) - 1:
                return 1
            result = traverse(idx + 1)
            if 10 <= int(s[idx:idx + 2]) <= 26:
                result += traverse(idx + 2)
            memo[idx] = result
            return result



        return traverse(0)