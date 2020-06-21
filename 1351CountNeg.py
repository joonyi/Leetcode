"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.
"""

from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    cnt += 1

        return cnt

        # return sum(a < 0 for row in grid for a in row)

    def countNegatives2(self, grid):
        def bin_search(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(row) - start

        cnt = 0
        for row in grid:
            cnt += bin_search(row)
        return cnt


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(Solution().countNegatives2(grid))

