class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        leftMax = 0
        rightMax = 0
        leftIdx = 0
        rightIdx = len(height) - 1
        while leftIdx < rightIdx:
            left = height[leftIdx]
            right = height[rightIdx]

            if left < right:
                if left < leftMax: # if descending and right already < left  => cavity
                    total += leftMax - left
                leftMax = max(leftMax, left)
                leftIdx += 1
            else:
                if right < rightMax: # if right side is descending and it is lower than left
                    total += rightMax - right
                rightMax = max(rightMax, right)
                rightIdx -= 1

        return total


