"""
Given an integer n, return any array containing n unique integers such that they add up to 0.
"""

from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        if n % 2 == 1:
            i = 1
        else:
            i = 0

        x = 1
        toggle = 0
        while i < n:
            res[i] = x
            if toggle:
                x = x * -1 + 1
            else:
                x = x * -1
            toggle ^= 1
            i += 1

        return res

    def sumZero2(self, n):
        # Any arithmetic sequence must have unique values if the common delta is non-zero
        # We need the sequence sum, so that (a[0] + a[n-1]) * n / 2 = 0, which means
        # a[0] + a[n-1] = 0
        # Also a[n-1] - a[0] = (n-1) * delta, solve two equations, 2*a[n-1] = d*(n-1)
        # if d = 2, a[n-1] is n - 1 and a[0] = -a[n-1] which is 1 - n
        res = list(range(1 - n, n, 2))
        # res = list(range(2 - 2*n, 2*n - 2 + 1, 4))
        return res


n = 5  # [-4, -2, 0, 2, 4], [0, 1, -1, 2, -2]
print(Solution().sumZero(n))
