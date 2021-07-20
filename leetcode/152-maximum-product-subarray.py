class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not len(nums):
            return 0

        maxTotal = nums[0]
        maxCurrent = nums[0]
        minCurrent = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            newMaxCurrent = max(num, num * maxCurrent, num * minCurrent)
            minCurrent = min(num, num * maxCurrent, num * minCurrent)
            maxCurrent = newMaxCurrent
            maxTotal = max(maxTotal, maxCurrent)

        return maxTotal