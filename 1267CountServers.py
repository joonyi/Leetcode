"""
You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
"""
class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        servers = []
        rows = dict()
        cols = dict()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    servers.append([i, j])
                    rows[i] = rows.get(i, 0) + 1
                    cols[j] = cols.get(j, 0) + 1
        cnt = 0
        for i, j in servers:
            if rows[i] > 1 or cols[j] > 1:
                cnt += 1

        return cnt

    def countServers2(self, grid):
        # m, n = len(grid), len(grid[0])
        # rows = [0] * m
        # cols = [0] * n
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]:
        #             rows[i] += 1
        #             cols[j] += 1
        rows = list(map(sum, grid))  # Equivalent to action above
        cols = list(map(sum, zip(*grid)))
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (rows[i] > 1 or cols[j] > 1):
                    cnt += 1
        return cnt

grid = [[1,0],[0,1]]  # 0
# grid = [[1,0],[1,1]]  # 3
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]  # 4
# grid = [[1]]
print(Solution().countServers2(grid))
