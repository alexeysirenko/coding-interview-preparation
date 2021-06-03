import random


class Solution:

    def __init__(self, w: List[int]):
        self.cumulativeSums = []
        self.totalSum = 0
        # [1, 3, 1] -> [1, 4, 5]
        # рандом потом выбираем в пределах от 0 до 5
        # по итогу будет что индекс 0 для рандома в пределах от 0 до 1
        # индекс 1 для рандома в пределах от 1 до 4
        # а индекс 2 для рандома в пределах от 4 до 5
        for num in w:
            self.totalSum += num
            self.cumulativeSums.append(self.totalSum)


    def pickIndex(self) -> int:
        rnd = random.random() * self.totalSum
        # находим в какой диапазон угодил наш рандом (от 0 до 5)
        for i, cumSum in enumerate(self.cumulativeSums):
            if rnd < cumSum:
                return i
        return len(self.cumulativeSums) - 1




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()