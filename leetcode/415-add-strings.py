from collections import deque

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def charToInt(c: str) -> int:
            return ord(c[0]) - ord('0')

        def traverse(idx1, idx2, carry, que):
            if idx1 < 0 and idx2 < 0:
                if carry:
                    que.append(str(carry))
                return que

            n1 = charToInt(num1[idx1]) if idx1 >= 0 else 0
            n2 = charToInt(num2[idx2]) if idx2 >= 0 else 0

            sum = n1 + n2 + carry

            n3 = sum % 10
            carry = sum // 10

            que.append(str(n3))

            return traverse(idx1 - 1, idx2 - 1, carry, que)

        return ''.join(reversed(traverse(len(num1) - 1, len(num2) - 1, 0, deque())))



