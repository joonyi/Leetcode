"""
There are two types of soup: type A and type B. Initially we have N ml of each type of soup.
There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B
Serve 75 ml of soup A and 25 ml of soup B
Serve 50 ml of soup A and 50 ml of soup B
Serve 25 ml of soup A and 75 ml of soup B
When we serve some soup, we give it to someone and we no longer have it.  Each turn, we will choose
from the four operations with equal probability 0.25. If the remaining volume of soup is not enough
to complete the operation, we will serve as much as we can.  We stop once we no longer have some
quantity of both types of soup.

Note that we do not have the operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become
empty at the same time.
"""


class Solution:
    def soupServings(self, N: int) -> float:
        Q, R = divmod(N, 25)
        N = Q + (R > 0)
        if N >= 500: return 1

        memo = {}

        def dp(x, y):
            if (x, y) not in memo:
                if x <= 0 and y <= 0:
                    ans = 0.5  # half the probability that A and B become empty at the same time
                elif x <= 0:
                    ans = 1.0  # A empty first
                elif y <= 0:
                    ans = 0.0  # B empty first
                else:
                    # dp(x - 4, y) means take the first operation
                    # dp(x - 3, y - 1), dp(x - 2, y - 2), dp(x - 1, y - 3) for other three
                    ans = 0.25 * (dp(x - 4, y) + dp(x - 3, y - 1) + dp(x - 2, y - 2) + dp(x - 1, y - 3))
                memo[x, y] = ans
            return memo[x, y]

        return dp(N, N)


N = 50  # 0.625
# N = 100
print(Solution().soupServings(N))

