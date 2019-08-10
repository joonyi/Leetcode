"""
You have a total of n coins that you want to form in a staircase shape,
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        coin = 1
        count = 0
        while n >= 0:
            n = n - coin
            coin += 1
            count += 1

        return count-1

    # n => x(x+1)/2, solve for x
    # 2n => x^2 + x
    # x^2 + x+ 1/4 <= 2n + 1/4
    # (x + 1/2)^2 <= 2n + 1/4
    # (x + 0.5) = sqrt(2n + 0.25)
    # x = -0.5 + sqrt(2n + 0.25)
    def arrangeCoins2(self, n):
        x = (2*n + 0.25)**0.5 - 0.5
        return int(x)


n = 8
print(Solution().arrangeCoins2(n))
