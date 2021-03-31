class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestBuyValue = prices[0]
        maxProfit = 0
        for currValue in prices:
            if currValue < lowestBuyValue:
                lowestBuyValue = currValue
            currProfit = currValue - lowestBuyValue
            if currProfit > maxProfit:
                maxProfit = currProfit
        return maxProfit
