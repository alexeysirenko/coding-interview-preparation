import re
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        operators = set(['+', '-', '*', '/'])
        parentheses = set(['(', ')'])

        priorities = {
            '+': 0,
            '-': 0,
            '*': 1,
            '/': 1
        }

        parser = re.compile('\d+|\S')

        parsed = parser.findall(s)

        print(parsed)

        def doMath(first, second, operator):
            if operator == '+':
                return int(first) + int(second)
            elif operator == '-':
                return int(first) - int(second)
            elif operator == '*':
                return int(first) * int(second)
            elif operator == '/':
                return int(first) / int(second)

        operatorsStack = deque()
        numbersStack = deque()

        i = 0
        while i < len(parsed):
            curr = parsed[i]
            if curr.lstrip('-').isdigit():
                numbersStack.append(curr)
            elif curr in operators:
                if curr == '-' and (i == 0 or parsed[i - 1] == '('):
                    numbersStack.append(0)

                if not operators:
                    operatorsStack.append(curr)
                else:
                    while operatorsStack and operatorsStack[-1] in operators and curr in operators and priorities[operatorsStack[-1]] >= priorities[curr]:
                        second, first = numbersStack.pop(), numbersStack.pop()
                        operator = operatorsStack.pop()
                        numbersStack.append(doMath(first, second, operator))
                    operatorsStack.append(curr)

            elif curr in parentheses:
                if curr == '(':
                    operatorsStack.append(curr)
                elif curr == ')':
                    while operatorsStack[-1] != '(':
                        second, first = numbersStack.pop(), numbersStack.pop()
                        operator = operatorsStack.pop()
                        numbersStack.append(doMath(first, second, operator))
                    operatorsStack.pop() # del opening parentheses
            i += 1

        #print(operatorsStack)
        #print(numbersStack)
        while operatorsStack:
            second, first = numbersStack.pop(), numbersStack.pop()
            operator = operatorsStack.pop()
            numbersStack.append(doMath(first, second, operator))

        return numbersStack[-1]








