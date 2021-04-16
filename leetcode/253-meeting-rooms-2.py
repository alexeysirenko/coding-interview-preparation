class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = 0, 1

        starts = sorted(i[start] for i in intervals)
        ends = sorted(i[end] for i in intervals)

        nRooms = 0
        startIdx = 0
        endIdx = 0
        while startIdx < len(starts) and endIdx < len(ends):
            currStart = starts[startIdx]
            nRooms += 1 # for new start -> new room

            currEnd = ends[endIdx]
            if currEnd <= currStart: # if at the moment of start some other meeting hava ended
                nRooms -= 1
                endIdx += 1

            startIdx += 1

        return nRooms