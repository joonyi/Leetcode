"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * 2 ** n
        for i in range(2 ** n):
            res[i] = i ^ (i >> 1)
        return res

    def grayCode2(self, n):
        results = [0]
        for i in range(n):
            results += [x + pow(2, i) for x in reversed(results)] # change + or | also fine
        return results

n = 3
print(Solution().grayCode2(n))