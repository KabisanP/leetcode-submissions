class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    maxProfit = max(maxProfit, prices[j] - prices[i])

        return maxProfit
