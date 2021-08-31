class HitCounter:


    def __init__(self):
        self.hits = []


    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)


    def getHits(self, timestamp: int) -> int:
        while self.hits:
            if self.hits[0] <= timestamp - 300:
                del self.hits[0]
            else:
                break
        return len(self.hits)



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)