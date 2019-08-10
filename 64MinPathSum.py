"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        path = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    path[i][j] = grid[i][j]
                elif j == 0:
                    path[i][j] = path[i - 1][j] + grid[i][j]
                elif i == 0:
                    path[i][j] = path[i][j - 1] + grid[i][j]
                else:
                    path[i][j] = min(path[i - 1][j], path[i][j - 1]) + grid[i][j]

        return path[m-1][n-1]


# grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2],[5,6],[1,1]]
print(Solution().minPathSum(grid))
