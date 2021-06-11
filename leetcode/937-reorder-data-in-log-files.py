from functools import cmp_to_key

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def identifierAndBody(s: str):
            i = s.find(' ')
            identifier = s[:i - 1]
            body = s[i + 1:]
            return identifier, body

        def isBodyLetter(b: str) -> bool:
            return b and b[0][0].isalpha()



        def compare2(first: str, second: str) -> int:
            firstIdentifier, firstBody = identifierAndBody(first)
            secondIdentifier, secondBody = identifierAndBody(second)

            isFirstLetter = isBodyLetter(firstBody)
            isSecondLetter = isBodyLetter(secondBody)

            if isFirstLetter and isSecondLetter:
                if firstBody < secondBody:
                    return -1
                elif firstBody > secondBody:
                    return 1
                else:
                    if firstIdentifier < secondIdentifier:
                        return -1
                    elif firstIdentifier > secondIdentifier:
                        return 1
                    else:
                        return 0

            elif isFirstLetter and not isSecondLetter:
                return -1
            elif not isFirstLetter and isSecondLetter:
                return 1
            else:
                return 0




        return sorted(logs, key = cmp_to_key(compare2))