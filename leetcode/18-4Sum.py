class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def kSum(fromIdx, toIdx, target: int, k: int) -> List[List[int]]:
            if toIdx - fromIdx + 1 < k or nums[fromIdx] * k > target or nums[toIdx] * k < target:
                return []
            if k == 2:
                return twoSum(fromIdx, toIdx, target)
            else:
                results = []
                for idx in range(fromIdx, toIdx + 1):
                    if idx == fromIdx or nums[idx - 1] != nums[idx]:
                        newTarget = target - nums[idx]
                        subResults = kSum(idx + 1, toIdx, newTarget, k - 1)
                        for subResult in subResults:
                            results.append([nums[idx]] + subResult)
                return results

        def twoSum(fromIdx, toIdx, target: int) -> List[List[int]]:
            leftIdx = fromIdx
            rightIdx = toIdx
            results = []
            while leftIdx < rightIdx:
                if fromIdx < leftIdx and nums[leftIdx - 1] == nums[leftIdx]:
                    leftIdx += 1
                elif rightIdx < toIdx and nums[rightIdx] == nums[rightIdx + 1]:
                    rightIdx -= 1
                else:
                    total = nums[leftIdx] + nums[rightIdx]
                    if total < target:
                        leftIdx += 1
                    elif total > target:
                        rightIdx -= 1
                    else:
                        results.append([nums[leftIdx], nums[rightIdx]])
                        leftIdx += 1
                        rightIdx -= 1
            return results

        nums.sort()
        return kSum(0, len(nums) - 1, target, 4)