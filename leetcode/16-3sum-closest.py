import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        smallestDiff = math.inf
        for leftIdx in range(len(nums) - 2):
            left = nums[leftIdx]
            if leftIdx == 0 or (leftIdx > 0 and nums[leftIdx - 1] != left):
                middleIdx = leftIdx + 1
                rightIdx = len(nums) - 1
                while middleIdx < rightIdx:
                    middle = nums[middleIdx]
                    right = nums[rightIdx]
                    currDiff = target - (left + middle + right)
                    if currDiff == 0:
                        return target - currDiff
                    elif abs(currDiff) < abs(smallestDiff):
                        smallestDiff = currDiff

                    if currDiff > 0:
                        middleIdx += 1
                    else:
                        rightIdx -= 1

        return target - smallestDiff
