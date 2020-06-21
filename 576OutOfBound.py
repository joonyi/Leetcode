"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball,
you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right).
However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary.
The answer may be very large, return it after mod 109 + 7.
"""


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # Brute Force
        if i == -1 or j == -1 or i == m or j == n:
            return 1

        cnt = 0
        if N != 0:
            cnt += self.findPaths(m, n, N - 1, i - 1, j)  # up
            cnt += self.findPaths(m, n, N - 1, i + 1, j)  # down
            cnt += self.findPaths(m, n, N - 1, i, j - 1)  # left
            cnt += self.findPaths(m, n, N - 1, i, j + 1)  # right
        return cnt

    def findPaths2(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def move(m, n, N, i, j, memo):
            if N < 0:
                return 0
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            stat = (i, j, N)
            if stat in memo:
                return memo[stat]

            up = move(m, n, N - 1, i - 1, j, memo)
            down = move(m, n, N - 1, i + 1, j, memo)
            left = move(m, n, N - 1, i, j - 1, memo)
            right = move(m, n, N - 1, i, j + 1, memo)
            ans = (up + down + left + right) % 1000000007
            memo[stat] = ans
            return ans

        memo = dict()
        return move(m, n, N, i, j, memo)

    def findPaths3(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # Idea 3 and 4 is the same
        cur_dp = [[0] * n for _ in range(m)]
        cur_dp[i][j] = 1
        cnt = 0
        for _ in range(N):
            prev_dp = cur_dp.copy()
            cur_dp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if prev_dp[i][j] > 0:
                        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            x = i + d[0]
                            y = j + d[1]
                            if 0 <= x < m and 0 <= y < n:
                                cur_dp[x][y] += prev_dp[i][j]
                                cur_dp[x][y] %= (10 ** 9 + 7)
                            else:
                                cnt += prev_dp[i][j]
                                cnt %= (10 ** 9 + 7)
        return cnt


    def findPaths4(self, m: int, n: int, N: int, i: int, j: int) -> int:
        x, y = i, j
        dp = [[[0] * n for _ in range(m)] for _ in range(N + 1)]
        for k in range(1, N + 1):
            for j in range(n):
                for i in range(m):
                    for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if -1 < a < m and -1 < b < n:  # inside boundary
                            dp[k][i][j] += dp[k - 1][a][b]
                            dp[k][i][j] %= 1000000007
                        else:  # Fall out of boundary
                            dp[k][i][j] += 1
                            dp[k][i][j] %= 1000000007
        return dp[N][x][y]


m, n, N, i, j = 2, 2, 2, 0, 0  # 6
# m, n, N, i, j = 1, 3, 3, 0, 1  # 12
# m, n, N, i, j = 8, 7, 16, 1, 5  # 102984580
# m, n, N, i, j = 8, 50, 23, 5, 26  # 914783380
# m, n, N, i, j = 36, 5, 50, 15, 3  # 390153306
print(Solution().findPaths3(m, n, N, i, j))

