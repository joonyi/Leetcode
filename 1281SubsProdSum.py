"""
Given an integer number n, return the difference between the product of its
digits and the sum of its digits.
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums = 0
        prod = 1
        while n > 0:
            d = n % 10
            prod *= d
            sums += d

            n //= 10

        return prod - sums

n = 234
n = 4421
print(Solution().subtractProductAndSum(n))