class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = float("+inf")
        maxProfit = 0
        todayProfit = 0
        for i in range(len(prices)):
            mini = min(mini, prices[i])
            todayProfit = prices[i] - mini
            maxProfit = max(maxProfit, todayProfit)
        return maxProfit