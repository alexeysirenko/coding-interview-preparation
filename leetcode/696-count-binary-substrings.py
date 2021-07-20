class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                left = i
                right = i + 1
                while left >= 0 and right < len(s):
                    if s[left] == s[i] and s[right] == s[i + 1]:
                        result += 1
                        left -= 1
                        right += 1
                    else:
                        break

        return result