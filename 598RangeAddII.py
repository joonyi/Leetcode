"""
Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with
two positive integers a and b, which means M[i][j] should be added by one for all
0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing
all the operations.
"""
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # Brute force, TLE
        mat = [[0 for _ in range(n)] for _ in range(m)]

        for row, col in ops:
            for i in range(row):
                for j in range(col):
                    mat[i][j] += 1

        maxVal = mat[0][0]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == maxVal:
                    cnt += 1
        return cnt

    def maxCount2(self, m, n, ops):
        for op in ops:
            m = min(m, op[0]) # get the min among all m
            n = min(n, op[1])

        # m and n now is the overlap region
        return m * n

m, n, ops = 3, 3, [[2,2],[3,3]]
print(Solution().maxCount2(m, n, ops))


