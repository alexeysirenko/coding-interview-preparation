class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for firstIdx in range(len(nums)):
            # check for the same nums in a row to avoid duplicated triplets
            if firstIdx == 0 or nums[firstIdx - 1] != nums[firstIdx]:
                secondIdx = firstIdx + 1
                thirdIdx = len(nums) - 1
                while secondIdx < thirdIdx and secondIdx < len(nums) and thirdIdx > firstIdx:
                    if nums[firstIdx] + nums[secondIdx] + nums[thirdIdx] > 0:
                        thirdIdx -= 1
                    elif nums[firstIdx] + nums[secondIdx] + nums[thirdIdx] < 0:
                        secondIdx += 1
                    else:
                        results.append([nums[firstIdx], nums[secondIdx], nums[thirdIdx]])
                        thirdIdx -=1
                        secondIdx += 1
                        # check for the same nums in a row to avoid duplicated triplets
                        while secondIdx < len(nums) and nums[secondIdx] == nums[secondIdx - 1]:
                            secondIdx += 1

        return results
