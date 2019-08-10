"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""

class Solution(object):
    def coinChange(self, coins, amount):
        if amount < 0:
            return 0

        def fewest(coins, rem, count):
            if rem < 0: return -1
            if rem == 0: return 0
            if count[rem-1] != 0:
                return count[rem - 1]

            min = float('inf')
            for coin in coins:
                res = fewest(coins, rem-coin, count)
                if res >= 0 and res < min:
                    min = 1 + res
            count[rem - 1] = -1 if min == float('inf') else min
            return count[rem - 1]

        return fewest(coins, amount, [0]*amount)

    # Amount outer loop
    def coinChange2(self, coins, amount):
        f = [amount + 1] * (amount + 1)
        f[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    f[i] = min(f[i], f[i - coin] + 1)

        if f[amount] > amount:
            return -1
        else:
            return f[amount]

    # coins outer loop
    def coinChange3(self, coins, amount):
        f = [amount + 1] * (amount + 1)
        f[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                f[i] = min(f[i], f[i-coin] + 1)
        return f[amount] if f[amount] <= amount else -1



# coins = [1,2,5] # 3
# amount = 11
# coins = [2] # -1
# amount = 3
coins = [2,5,10,1] # 4
amount = 27
# coins = [186,419,83,408] # expect 20
# amount = 6249

print(Solution().coinChange3(coins, amount))