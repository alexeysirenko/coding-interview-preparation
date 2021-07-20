class Solution:
    def romanToInt(self, s: str) -> int:
        charValues = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }

        total = charValues[s[-1]]

        for i in reversed(range(len(s) - 1)):
            if charValues[s[i]] < charValues[s[i + 1]]:
                total -= charValues[s[i]]
            else:
                total += charValues[s[i]]

        return total