class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for i in range(len(s)):
            if not s[i] in counter:
                counter[s[i]] = 0
            if not t[i] in counter:
                counter[t[i]] = 0

            counter[s[i]] += 1
            counter[t[i]] -= 1

        for key, count in counter.items():
            if count != 0:
                return False
        return True