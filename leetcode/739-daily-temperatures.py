from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nextDayTemp, nextDay = 0, 1
        nTotalDays = len(temperatures)
        warmerDays = deque() # every item there is warmer than current day
        daysToWait = [0] * nTotalDays # result days to wait for a warmer temp
        for day in range(nTotalDays - 1, -1, -1): # from end to start
            while warmerDays and warmerDays[0][nextDayTemp] <= temperatures[day]:
                    del warmerDays[0] # delete all days colder than current
            if warmerDays: # every day in stack (i.e. in future) is warmer than current. Pick closest one
                daysToWait[day] = warmerDays[0][nextDay] - day

            warmerDays.appendleft([temperatures[day], day])
                
        return daysToWait