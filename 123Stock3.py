"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock
before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0
        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2

    def maxProfit2(self, prices):
        # TLE for Stock 4
        # dp[k][i] max profit for k transactions on i-th day
        if len(prices) == 0: return 0
        dp = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            for i in range(1, len(prices)):
                minp = prices[0]
                for j in range(1, i + 1):
                    minp = min(minp, prices[j] - dp[k-1][j-1])
                    dp[k][i] = max(dp[k][i-1], prices[i] - minp)

        return dp[2][len(prices)-1]

prices = [3,3,5,0,0,3,1,4] # 6
prices = [2,5,7,1,4,3,1,3] # 8
# prices = [3,2,6,5,0,3] # 7
print(Solution().maxProfit(prices))