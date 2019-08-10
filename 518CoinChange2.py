"""
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        f = [0] * (amount + 1)
        f[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                f[i] = f[i] + f[i - coin]

        return f[amount]


# coins = [1,2,5]
# amount = 5
coins = [2]
amount = 3
# coins = [10]
# amount = 10
print(Solution().change(amount, coins))