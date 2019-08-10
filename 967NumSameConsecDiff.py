"""
Return all non-negative integers of length N such that the absolute difference between
every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself.
For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.
"""

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        # A = [x for x in range(10**(N-1), 10**(N))]
        # print(A)
        diff = {}
        for i in range(10):
            if i + K < 10:
                diff[i] = i + K
            if i - K >= 0:
                diff[i] = i - K
        print(diff)

        res = []
        for i in range(10):
            if i != 0 and (i + K < 10 or i - K >= 0):
                res.append(i)

        for _ in range(1, N):
            for i, num in enumerate(res):
                res[i] = num*10 + diff[num%10]

        return res

if
# N = 3
# K = 7
N = 2
K = 1
# [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
print(Solution().numsSameConsecDiff(N, K))