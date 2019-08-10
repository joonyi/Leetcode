"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that
each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
(Each subgrid is contiguous).
"""
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3: return 0

        cnt = 0
        for i in range(m - 2):
            for j in range(n - 2):
                if self.isMagic(grid, i, j):
                    cnt += 1

        return cnt

    def isMagic(self, grid, i, j):
        if grid[i][j] + grid[i+2][j+2] != 10:
            return False
        elif grid[i][j+2] + grid[i+2][j] != 10:
            return False

        ele = set()
        for p in range(i, i + 3):
            ele.add(grid[p][j])
            ele.add(grid[p][j+1])
            ele.add(grid[p][j+2])
            if grid[p][j] + grid[p][j+1] + grid[p][j+2] != 15:
                return False

        if {1,2,3,4,5,6,7,8,9} != ele:
            return False

        for p in range(j, j + 3):
            if grid[i][p] + grid[i+1][p] + grid[i+2][p] != 15:
                return False

        return True

# grid = [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# grid = [[5,5,5],
#         [5,5,5],
#         [5,5,5]]
grid = [[1,8,6],[10,5,0],[4,2,9]]
print(Solution().numMagicSquaresInside(grid))