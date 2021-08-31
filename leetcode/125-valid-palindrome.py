class Solution:
    def isPalindrome(self, s: str) -> bool:
        leftIdx, rightIdx = 0, len(s) - 1
        while leftIdx <= rightIdx:
            left = s[leftIdx]
            right = s[rightIdx]
            if not left.isalnum():
                leftIdx += 1
            elif not right.isalnum():
                rightIdx -= 1
            else:
                if right.lower() != left.lower():
                    return False
                else:
                    rightIdx -= 1
                    leftIdx += 1

        return True
