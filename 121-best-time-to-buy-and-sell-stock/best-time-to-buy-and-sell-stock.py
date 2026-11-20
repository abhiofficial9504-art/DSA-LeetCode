class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mini = float("inf")
        today_profit = 0
        max_profit = 0

        for i in range(len(prices)):
            mini = min(mini, prices[i])
            today_profit = prices[i] - mini
            max_profit = max(max_profit, today_profit)
        return max_profit
