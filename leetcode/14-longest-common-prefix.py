class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for charIdx in range(len(strs[0])):
            currChar = strs[0][charIdx]
            for strIdx in range(1, len(strs)):
                str = strs[strIdx]
                if charIdx >= len(str) or str[charIdx] != currChar:
                    return strs[0][:charIdx]
        return strs[0]
