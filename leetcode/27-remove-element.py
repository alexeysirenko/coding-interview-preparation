class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first, last = 0, len(nums) - 1
        while first <= last:
            if nums[first] == val:
                nums[first] = nums[last]
                last -= 1
            else:
                first += 1

        return last + 1
