class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if len(nums) < 2:
            return nums

        leftIdx, rightIdx = 0, n
        result = [0 for _ in range(len(nums))]
        i = 0
        while rightIdx < len(nums):
            result[i] = nums[leftIdx]
            result[i + 1] = nums[rightIdx]
            leftIdx += 1
            rightIdx += 1
            i += 2

        return result
