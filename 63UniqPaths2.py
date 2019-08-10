"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        path = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                elif i == 0 and j == 0:
                    path[i][j] = 1
                elif i == 0:
                    path[i][j] += path[i][j - 1]
                elif j == 0:
                    path[i][j] += path[i - 1][j]
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1]

        return path[m - 1][n - 1]

    # in-place
    def uniquePathsWithObstacles2(self, obstacleGrid):
        if not obstacleGrid:
            return
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, r):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, c):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, r):
            for j in range(1, c):
                obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid


obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# obstacleGrid = [[0,0]]
# obstacleGrid = [[0],[0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))