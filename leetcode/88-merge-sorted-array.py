class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1, idx2 = m - 1, n - 1
        currIdx = len(nums1) - 1
        while (idx1 >= 0 or idx2 >= 0) and currIdx >= 0:
            num1 = nums1[idx1] if idx1 >= 0 else -math.inf
            num2 = nums2[idx2] if idx2 >= 0 else -math.inf
            if num1 > num2:
                nums1[currIdx] = num1
                idx1 -= 1
            else:
                nums1[currIdx] = num2
                idx2 -= 1
            currIdx -= 1



