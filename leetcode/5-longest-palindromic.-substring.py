class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLeft, maxRight = 0, 0
        for idx in range(len(s)):
            for shift in range(2):
                left = idx
                right = idx + shift

                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > maxRight - maxLeft + 1:
                        maxLeft, maxRight = left, right
                    left -= 1
                    right += 1

        return s[maxLeft:maxRight + 1]


