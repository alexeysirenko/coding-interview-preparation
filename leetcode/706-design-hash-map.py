class MyHashMap:

    def __hash(self, key: int) -> int:
        return key % len(self.arr)

    def __init__(self):
        self.arr = [[] for _ in range(10000)]


    def put(self, key: int, value: int) -> None:
        self.remove(key)
        hs = self.__hash(key)
        self.arr[hs].append([key, value])


    def get(self, key: int) -> int:
        hs = self.__hash(key)
        elems = self.arr[hs]
        for elem in elems:
            if elem[0] == key:
                return elem[1]
        return -1


    def remove(self, key: int) -> None:
        hs = self.__hash(key)
        elems = self.arr[hs]
        #print(key, hs, len(self.arr), elems)
        for elemIdx in range(len(elems)):
            if len(elems[elemIdx]) > 0 and elems[elemIdx][0] == key:
                del elems[elemIdx]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)