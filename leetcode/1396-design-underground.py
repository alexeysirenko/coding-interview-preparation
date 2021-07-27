class UndergroundSystem:



    def __init__(self):
        self.checkins = {}
        self.travelTimes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStationName, startTime = self.checkins[id]
        if not startStationName in self.travelTimes:
            self.travelTimes[startStationName] = {}
        if not stationName in self.travelTimes[startStationName]:
            self.travelTimes[startStationName][stationName] = (0, 0)
        total, N = self.travelTimes[startStationName][stationName]
        self.travelTimes[startStationName][stationName] = (total + (t - startTime), N + 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not startStation in self.travelTimes:
            return 0.0
        if not endStation in self.travelTimes[startStation]:
            return 0.0

        total, N = self.travelTimes[startStation][endStation]
        return total / N



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)