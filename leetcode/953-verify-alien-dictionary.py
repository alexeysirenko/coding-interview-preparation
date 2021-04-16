class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}
        for idx, char in enumerate(order):
            orderMap[char] = idx

        for currWordIdx in range(1, len(words)):
            currWord = words[currWordIdx]
            prevWord = words[currWordIdx - 1]

            for charIdx in range(max(len(currWord), len(prevWord))):
                currOrderIdx = orderMap[currWord[charIdx]] if charIdx < len(currWord) else -1
                prevOrderIdx = orderMap[prevWord[charIdx]] if charIdx < len(prevWord) else -1

                if currOrderIdx != prevOrderIdx:
                    if prevOrderIdx <= currOrderIdx:
                        break
                    return False

        return True