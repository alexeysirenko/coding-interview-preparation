class Solution:
    def myPow(self, x: float, n: int) -> float:

        def traverse(x: float, n: int) -> float:
            if n == 0:
                return 1
            half = traverse(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            return 1 / traverse(x, -n)
        else:
            return traverse(x, n)