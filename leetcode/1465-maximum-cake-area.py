class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        maxHorSlice = 0
        for i in range(len(horizontalCuts) + 1):
            prevCut = horizontalCuts[i - 1] if i > 0 else 0
            currCut = horizontalCuts[i] if i < len(horizontalCuts) else h
            #print(prevCut, currCut)
            maxHorSlice = max(maxHorSlice, currCut - prevCut)

        #print(maxHorSlice)

        maxVertSlice = 0
        for i in range(len(verticalCuts) + 1):
            prevCut = verticalCuts[i - 1] if i > 0 else 0
            currCut = verticalCuts[i] if i < len(verticalCuts) else w
            #print(prevCut, currCut)
            maxVertSlice = max(maxVertSlice, currCut - prevCut)

        #print(maxHorSlice, maxVertSlice)
        return (maxHorSlice * maxVertSlice) % (10 ** 9 + 7)
