from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openingIdxs = deque()
        idxToRemove = set()
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                openingIdxs.appendleft(i) # index of the opening
            # для каждой закрывающей должна быть открывающая
            # если для закрывающей нет открывающей - удаляем закрывающую
            elif char == ')' and not openingIdxs:
                idxToRemove.add(i)
            # если нашлась закрывающая из открывающей
            elif char == ')' and openingIdxs:
                openingIdxs.popleft()

        idxToRemove = idxToRemove.union(set(openingIdxs))

        result = []
        for i in range(len(s)):
            if not i in idxToRemove:
                result.append(s[i])

        return ''.join(result)
