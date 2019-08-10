"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num
calculate the number of 1's in their binary representation and return them as an array.
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        from math import log2
        res = [0] * (num + 1)
        for n in range(1, num + 1):
            if n % 2 == 1:
                res[n] = res[n-1] + 1
            else:
                if n & (n - 1) == 0: # test if power of 2
                    res[n] = 1
                else:
                    res[n] = res[n >> 1]

        return res

    def countBits2(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        for n in range(1, num + 1):
            # res[n] = res[n // 2] + n % 2
            # res[n] = res[n >> 1] + (n & 1)
            res[n] = res[n & (n - 1)] + 1 # this is fastest
        return res

num = 16
print(Solution().countBits2(num))