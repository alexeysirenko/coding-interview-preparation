class Solution:
    def compress(self, chars: List[str]) -> int:
        def flushChars(insertAt, char, nChars) -> int:
            chars[insertAt] = char
            insertAt += 1
            if nChars > 1:
                for nStr in str(nChars):
                    chars[insertAt] = nStr
                    insertAt += 1
            return insertAt


        insertIdx = 0
        currIdx = 0
        prevChar = None
        nChars = 0
        while currIdx < len(chars):
            currChar = chars[currIdx]
            if currChar != prevChar and nChars > 0:
                insertIdx = flushChars(insertIdx, prevChar, nChars)
                nChars = 0
            nChars += 1
            prevChar = currChar
            currIdx += 1

        if nChars > 0:
            insertIdx = flushChars(insertIdx, prevChar, nChars)

        return insertIdx