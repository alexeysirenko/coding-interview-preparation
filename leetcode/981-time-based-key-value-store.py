class TimeMap:

    def __init__(self):
        self.dict = {}

    def __binarySearch(self, start, end, arr, timestamp):
        val, ts = 0, 1
        if start > end:
            return ''
        if timestamp >= arr[end][ts]:
            return arr[end][val]
        else:
            mid = (start + end) // 2
            if arr[mid][ts] > timestamp:
                return self.__binarySearch(start, mid - 1, arr, timestamp)
            elif arr[mid][ts] < timestamp:
                return self.__binarySearch(start, mid, arr, timestamp)
            else:
                return arr[mid][val]



    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dict or not self.dict[key]:
            return ''
        else:
            arr = self.dict[key]
            return self.__binarySearch(0, len(arr) - 1, arr, timestamp)



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)