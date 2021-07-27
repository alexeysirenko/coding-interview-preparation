import re
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        priority = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1
        }

        def doMath(first, second, operator):
            first = int(first)
            second = int(second)
            if operator == '+':
                return first + second
            elif operator == '-':
                return first - second
            elif operator == '*':
                return first * second
            else:
                return first // second

        parser = re.compile('\d+|\S')
        parsed = parser.findall(s)

        numbers = deque()
        operators = deque()

        for curr in parsed:
            if curr.isdigit():
                numbers.append(int(curr))
            else:
                if not operators:
                    operators.append(curr)
                else:
                    while operators and priority[curr] <= priority[operators[-1]]:
                        second, first = numbers.pop(), numbers.pop()
                        operator = operators.pop()
                        numbers.append(doMath(first, second, operator))
                    operators.append(curr)

        while operators:
            second, first = numbers.pop(), numbers.pop()
            operator = operators.pop()
            numbers.append(doMath(first, second, operator))

        return numbers[-1]