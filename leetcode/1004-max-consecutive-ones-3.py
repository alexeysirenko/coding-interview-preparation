class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        nOnes = 0
        nZeros = 0
        leftIdx, rightIdx = 0, 0
        while leftIdx <= rightIdx and rightIdx < len(nums):
            if nums[rightIdx] == 1:
                nOnes += 1
            elif nums[rightIdx] == 0:
                nZeros += 1

            while nZeros > k and leftIdx <= rightIdx:
                if nums[leftIdx] == 1:
                    nOnes -= 1
                else:
                    nZeros -= 1
                leftIdx += 1


            result = max(result, nOnes + nZeros)
            rightIdx += 1

        return result