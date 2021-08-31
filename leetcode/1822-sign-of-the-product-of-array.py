class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            if num == 0:
                return 0
            else:
                if num < 0:
                    prod *= -1

        return prod


