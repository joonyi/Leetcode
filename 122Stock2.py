"""
Similar as stock1 but you may complete as many transactions as you like.

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution:
    # the points of interest are the consecutive valleys and peaks.
    # we need to consider every peak immediately following a valley to maximize the profit
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley

        return maxprofit


    def maxProfit2(self, prices):
        ret = 0
        for i in range(1,len(prices)):
            if prices[i] - prices[i-1] > 0:
                ret += prices[i] - prices[i-1]

        return ret

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))