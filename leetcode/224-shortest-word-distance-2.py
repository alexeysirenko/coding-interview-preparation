class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordIndex = {}
        for i in range(len(wordsDict)):
            if not wordsDict[i] in self.wordIndex:
                self.wordIndex[wordsDict[i]] = []

            self.wordIndex[wordsDict[i]].append(i)


    def shortest(self, word1: str, word2: str) -> int:
        idxs1 = self.wordIndex[word1]
        idxs2 = self.wordIndex[word2]
        i1 = 0
        i2 = 0
        shortest = math.inf
        while i1 < len(idxs1) and i2 < len(idxs2):
            shortest = min(shortest, abs(idxs1[i1] - idxs2[i2]))
            if shortest == 1:
                break

            if i1 < len(idxs1) - 1 and i2 < len(idxs2) - 1:
                if abs(idxs1[i1 + 1] - idxs2[i2]) > abs(idxs1[i1] - idxs2[i2 + 1]):
                    i2 += 1
                else:
                    i1 += 1
            elif i1 == len(idxs1) - 1 and i2 < len(idxs2) - 1:
                i2 += 1
            else:
                i1 += 1

        return shortest

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)