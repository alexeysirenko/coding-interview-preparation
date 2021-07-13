class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        memo = [0 for _ in range(len(nums))]
        memo[0] = nums[0]
        if len(nums) > 1:
            memo[1] = nums[1]

        for i in range(2, len(memo)):
            wPrev = nums[i] + (memo[i - 2] if i >= 2 else 0)
            wPrevPrev = nums[i] + (memo[i - 3] if i >= 3 else 0)
            memo[i] = max(wPrev, wPrevPrev)

        return max(memo[-1], memo[-2])