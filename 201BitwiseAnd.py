"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of
all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
            n = n & (n-1)
        return n

    # The operator & is keeping those bits which is 1 in every number.
    # This tells us, the bitwise and of the range is keeping the common bits of m and n
    # from left to right until the first bit that they are different, padding zeros for the rest.
    def rangeBitwiseAnd2(self, m, n):
        i = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            i += 1
        return n << i

m = 5
n = 7
print(Solution().rangeBitwiseAnd2(m, n))