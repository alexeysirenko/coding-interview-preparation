class Solution:
    def validPalindrome(self, s: str) -> bool:

        def traverse(s, nDeletions):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right] and nDeletions <= 0:
                    return False
                elif s[left] != s[right] and nDeletions > 0:
                    return traverse(s[left:right], nDeletions - 1) or traverse(s[left + 1:right + 1], nDeletions - 1)
                else:
                    left += 1
                    right -= 1
            if left >= right:
                return True
            return False

        return traverse(s, 1)
