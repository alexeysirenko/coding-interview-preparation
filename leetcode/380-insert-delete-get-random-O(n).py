import random

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.arr = []  # for O(1) random access


    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.arr.append(val)
            self.dict[val] = len(self.arr) - 1      # link to the element in array
            return True


    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        else:
            idx = self.dict[val]
            lastElement = self.arr[-1]
            self.arr[idx], self.arr[-1] = lastElement, val # swap
            self.arr.pop()
            self.dict[lastElement] = idx
            del self.dict[val]
            return True


    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()