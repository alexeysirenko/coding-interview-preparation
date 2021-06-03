class Solution:
    def decodeString(self, s: str) -> str:
        #print(s)
        def closingBracket(openIdx) -> int:
            balance = 0
            closeIdx = openIdx
            while closeIdx < len(s):
                if s[closeIdx] == '[':
                    balance += 1
                elif s[closeIdx] == ']':
                    balance -= 1
                    if balance == 0:
                        return closeIdx
                closeIdx += 1

        acc = ''
        leftIdx = 0
        nAccum = 0
        while leftIdx < len(s):
            char = s[leftIdx]
            if char.isalpha():
                acc = acc + char
            elif char.isnumeric():
                nAccum = nAccum * 10 + int(char)
            elif char == '[':
                rightIdx = closingBracket(leftIdx)
                acc = acc + nAccum * self.decodeString(s[leftIdx + 1:rightIdx])
                nAccum = 0
                leftIdx = rightIdx
            leftIdx += 1
        return acc
