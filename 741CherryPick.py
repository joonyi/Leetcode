"""
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.
"""
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Greedy wrong answer
        path = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        cherry = self.dp_path(grid, path)
        if cherry == 0: # Robot cannot get to end
            return 0

        i, j = len(grid) - 1, len(grid[0]) - 1
        grid[i][j] = 0
        while i != 0 or j != 0:
            if  j == 0:
                i -= 1
            elif i == 0:
                j -= 1
            elif path[i-1][j] > path[i][j-1]:
                i -= 1
            elif path[i - 1][j] < path[i][j - 1]:
                j -= 1
            grid[i][j] = 0

        path = [[0 for _ in range(len(grid))] for _ in range(len(grid[0]))]
        cherry += self.dp_path(grid, path)
        return cherry

    def dp_path(self, grid, path):
        m, n = len(path), len(path[0])
        cherry_path = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    continue
                if i == 0 and j == 0:
                    path[i][j] = grid[i][j]
                elif j == 0:
                    path[i][j] = path[i - 1][j] + grid[i][j]
                elif i == 0:
                    path[i][j] = path[i][j - 1] + grid[i][j]
                else:
                    if max(path[i - 1][j], path[i][j - 1]) == 0:
                        continue
                    path[i][j] = max(path[i - 1][j], path[i][j - 1]) + grid[i][j]

        return path[m-1][n-1]

    def cherryPickup2(self, grid):
        N = len(grid)
        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (N == r1 or N == r2 or N == c1 or N == c2 or
                        grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1, c1 + 1, c2 + 1), dp(r1 + 1, c1, c2 + 1),
                           dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2))

            memo[r1][c1][c2] = ans
            return ans

        return max(0, dp(0, 0, 0))

    def cherryPickup3(self, grid):
        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2 * N - 1):
            dp2 = [[float('-inf')] * N for _ in range(N)]
            for i in range(max(0, t - (N - 1)), min(N - 1, t) + 1):
                for j in range(max(0, t - (N - 1)), min(N - 1, t) + 1):
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    val = grid[i][t - i]
                    if i != j: val += grid[j][t - j]
                    dp2[i][j] = max(dp[pi][pj] + val
                                    for pi in (i - 1, i) for pj in (j - 1, j)
                                    if pi >= 0 and pj >= 0)
            dp = dp2
        return max(0, dp[N - 1][N - 1])

# grid =[[0, 1, -1],[1, 0, -1],[1, 1,  1]]
# grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
grid = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]


print(Solution().cherryPickup3(grid))