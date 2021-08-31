from heapq import *

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = {}
        for id, score in sorted(items, key=lambda item: item[0]):
            if not id in scores:
                scores[id] = []
            minHeap = scores[id]
            heappush(minHeap, score)
            if len(minHeap) > 5:
                heappop(minHeap)
        #print(scores)
        results = []
        for id in scores:
            avg = sum(scores[id]) // 5
            results.append([id, avg])

        return results