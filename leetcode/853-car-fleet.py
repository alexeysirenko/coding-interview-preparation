class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = sorted(zip(position, speed), reverse = True)
        #print(s)
        nFleets = 0
        prevArriveTime = 0
        for currPosition, currSpeed in s:
            currArriveTime = (target - currPosition) / currSpeed
            if prevArriveTime < currArriveTime:
                prevArriveTime = currArriveTime
                nFleets += 1

        return nFleets
