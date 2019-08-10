"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and
0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island).
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.
Determine the perimeter of the island.
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    neighbour = self.check(grid, i, j)
                    perimeter += 4 - neighbour

        return perimeter

    def check(self, grid, i, j):
        n = 0
        up, down = i - 1, i + 1
        right, left = j + 1, j - 1
        if up >= 0:
            if grid[up][j] == 1:
                n += 1
        if down < len(grid):
            if grid[down][j] == 1:
                n += 1
        if left >= 0:
            if grid[i][left] == 1:
                n += 1
        if right < len(grid[0]):
            if grid[i][right] == 1:
                n += 1

        return n

grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
grid2 = [[1]]

print(Solution().islandPerimeter(grid2))