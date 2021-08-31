class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertAt = 1
        firstUnique = 1
        while firstUnique < len(nums):
            if nums[firstUnique] != nums[firstUnique - 1]:
                nums[insertAt] = nums[firstUnique]
                insertAt += 1
            firstUnique += 1

        return insertAt


