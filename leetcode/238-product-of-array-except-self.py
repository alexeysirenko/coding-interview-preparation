class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1] # so as not to multiply to 0 at 1st pass

        # firstly left to right
        for i in range(1, len(nums)):
            leftProducts.append(leftProducts[i - 1] * nums[i - 1])

        # then right to left
        rightProduct = 1
        for i in reversed(range(len(nums))):
            leftProducts[i] = leftProducts[i] * rightProduct
            rightProduct *= nums[i]

        return leftProducts
