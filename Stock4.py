"""
Say you have an array for which the i-th element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        m = len(prices)
        if m == 0 or m == 1 or k == 0:
            return 0

        if k > m / 2: # for corner case speed up
            ans = 0
            for i in range(1, m):
                ans += max(prices[i] - prices[i-1], 0) # bcs k > m/2, just sell if any positive profit
            return ans

        buy =[[0] * (m + 1) for _ in range(k + 1)]
        sell = [[0] * (m + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            buy[i][0] = float('-inf')
        for i in range(1, m + 1):
            for j in range(1, k + 1):
                buy[j][i] = max(buy[j][i - 1], sell[j - 1][i - 1] - prices[i - 1])
                sell[j][i] = max(buy[j][i - 1] + prices[i - 1], sell[j][i - 1])

        return sell[k][m]

    def maxProfit2(self, k, prices):
        n = len(prices)
        if n == 0 or n == 1 or k == 0:
            return 0

        if k >= n / 2: # for corner case speed up
            ans = 0
            for i in range(1, n):
                ans += max(prices[i] - prices[i-1], 0) # bcs k > m/2, just sell if any positive profit
            return ans

        t = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            tmpMax = -prices[0] # money spend to buy stock, hence negative
            for j in range(1, n):
                t[i][j] = max(t[i][j - 1], prices[j] + tmpMax) # prices[j] + tmpMax means sell the stock
                tmpMax = max(tmpMax, t[i - 1][j - 1] - prices[j]) # buy the lowest stock. Maximize profit at hand
        return t[k][n - 1]


# prices, k = [2,4,1], 2
prices, k = [2,5,7,1,4,3,1,3], 2 # 8
# prices, k = [3,2,6,5,0,3], 2 # 7
print(Solution().maxProfit2(k, prices))