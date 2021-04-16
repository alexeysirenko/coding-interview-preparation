class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = {}
        memo[0] = 1
        sum = 0
        count = 0

        for num in nums:
            sum += num
            # если в memo есть отрезок sum - k, где sum - текущая сумма,
            # то значит что текущий отрезок равен k
            if sum - k in memo:
                count += memo[sum - k]
            if not sum in memo:
                memo[sum] = 0
            memo[sum] += 1

        return count

