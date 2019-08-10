"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 2^31.
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        res = 0
        while z > 0:
            res += z % 2
            z >>= 1
        return res

    def hammingDistance2(self, x, y):
        # slower
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y

x, y = 8, 7
print(Solution().hammingDistance2(x, y))