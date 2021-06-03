from collections import deque

class Logger:

    def __init__(self):
        self.msgWithin10MinsQueue = deque()
        self.msgsWithin10Mins = set()


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.msgWithin10MinsQueue:
            oldTimestamp, oldMsg = self.msgWithin10MinsQueue[0]
            if timestamp - oldTimestamp >= 10:
                self.msgWithin10MinsQueue.popleft()
                self.msgsWithin10Mins.remove(oldMsg)
            else:
                break

        if message not in self.msgsWithin10Mins:
            self.msgWithin10MinsQueue.append((timestamp, message))
            self.msgsWithin10Mins.add(message)
            return True
        else:
            return False
