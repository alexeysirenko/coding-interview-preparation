class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        nCharsQue = []
        charIdx = 0
        result = list(s)
        while charIdx < len(result):
            currChar = result[charIdx]
            prevChar = result[charIdx - 1] if charIdx > 0 else None
            prevCharCount = nCharsQue[-1] if nCharsQue else 0
            if currChar != prevChar:
                nCharsQue.append(1)
                charIdx += 1
            elif currChar == prevChar and prevCharCount + 1 < k:
                nCharsQue[-1] += 1
                charIdx += 1
            elif currChar == prevChar and prevCharCount + 1 == k:
                del nCharsQue[-1]
                del result[charIdx - k + 1: charIdx + 1]
                charIdx -= (k - 1)

        return ''.join(result)