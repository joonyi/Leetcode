class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        top = [0] * n
        left = [0] * m
        for i, row in enumerate(grid):
            left[i] = max(row)
            for j in range(len(row)):
                if row[j] > top[j]:
                    top[j] = row[j]

        incre = 0
        for i, row in enumerate(grid):
            for j in range(len(row)):
                incre += min(top[j], left[i]) - grid[i][j]

        return incre


grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(Solution().maxIncreaseKeepingSkyline(grid))