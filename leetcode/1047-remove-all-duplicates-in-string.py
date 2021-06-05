from collections import deque

class Solution:
    def removeDuplicates(self, s: str) -> str:
        que = deque()
        for char in s:
            prevChar = que[-1] if que else None
            if prevChar and prevChar == char:
                que.pop()
            else:
                que.append(char)

        return ''.join(que)
