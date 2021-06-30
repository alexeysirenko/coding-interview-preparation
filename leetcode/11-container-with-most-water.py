class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(l, r):
            return min(height[l], height[r]) * (r - l)

        bestLeft, bestRight = 0, len(height) - 1
        left, right = bestLeft, bestRight
        while left < right:
            if area(left, right) > area(bestLeft, bestRight):
                bestLeft, bestRight = left, right
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return area(bestLeft, bestRight)

