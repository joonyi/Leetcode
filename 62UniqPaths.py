"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    path[i][j] = 1
                elif i == 0:
                    path[i][j] += path[i][j-1]
                elif j == 0:
                    path[i][j] += path[i-1][j]
                else:
                    path[i][j] = path[i-1][j] + path[i][j-1]

        return path[n-1][m-1]


m = 3
n = 2
print(Solution().uniquePaths(m, n))
