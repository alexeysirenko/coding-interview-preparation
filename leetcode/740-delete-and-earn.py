from collections import OrderedDict

class Solution:

    def deleteAndEarn(self, nums):
        nOccurs = OrderedDict()
        for num in sorted(nums):
            if not num in nOccurs:
                nOccurs[num] = 0
            nOccurs[num] += 1

        uniqueValues = list(nOccurs.keys())
        valueCounts = list(nOccurs.values())
        memo = [0 for _ in range(len(nOccurs))]
        memo[0] = uniqueValues[0] * valueCounts[0]

        for i in range(1, len(memo)):
            if uniqueValues[i] - 1 == uniqueValues[i - 1]: # не можем взять предыдущее так как его пришлось бы удалить как смежное число
                ifWithCurrent = uniqueValues[i] * valueCounts[i] + (memo[i - 2] if i > 1 else 0)
                ifWithoutCurrent = memo[i - 1]
                memo[i] = max(ifWithCurrent, ifWithoutCurrent)
            else: # can pick prev or prev-prev
                memo[i] = uniqueValues[i] * valueCounts[i] + max(memo[i - 1], memo[i - 2])


        return memo[-1]
