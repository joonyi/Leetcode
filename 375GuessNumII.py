"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x.
You win the game when you guess the number I picked.
"""

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # Fail attempt
        if n == 1:
            return 0

        cost = 0
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            left = mid + 1
            cost += mid

        if n & 2 == 0:
            return cost - 1
        return cost

    def getMoneyAmount2(self, n: int) -> int:
        # need[lo][hi] -> minimum number of money to guarantee a win for the number from lo to hi
        need = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                # need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi])
                #                    for x in range(lo, hi))
                cost = []
                for x in range(lo, hi): # pick x and wrong
                    cost.append(x + max(need[lo][x - 1], need[x + 1][hi]))
                need[lo][hi] = min(cost)
        return need[1][n]

    def getMoneyAmount3(self, n: int) -> int:
        def dp(lo, hi):
            if lo >= hi:
                return 0
            if need[lo][hi] != 0:
                return need[lo][hi]
            cost = []
            for x in range(lo, hi):
                cost.append(x + max(dp(lo, x - 1), dp(x + 1, hi)))
            need[lo][hi] = min(cost)
            return need[lo][hi]

        need = [[0] * (n + 1) for _ in range(n + 1)]
        return dp(1, n)

    def getMoneyAmount4(self, n: int) -> int:
        def dp(lo, hi):
            if (lo, hi) not in memo:
                if lo >= hi:
                    memo[(lo, hi)] = 0
                else:
                    cost = []
                    for x in range(lo, hi):
                        cost.append(x + max(dp(lo, x - 1), dp(x + 1, hi)))
                    memo[(lo, hi)] = min(cost)

            return memo[(lo, hi)]

        memo = {}
        return dp(1, n)


# n = 10  # 16
# n = 4  # 4
# n = 1  # 0
# n = 3  # 2
n = 7  # 10
# n = 9  # 14

print(Solution().getMoneyAmount2(n))


