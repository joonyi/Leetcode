class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten = []
        fresh = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        dir = ((0, 1), (0, -1), (-1, 0), (1, 0))
        cnt = 0
        while rotten:
            nxt_rot = []
            cnt += 1
            for i, j in rotten:
                for d in dir:
                    x = i + d[0]
                    y = j + d[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        nxt_rot.append((x,y))
                        fresh -= 1
            rotten = nxt_rot

            if fresh == 0:
                return cnt

        return -1



# grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0,2]]
print(Solution().orangesRotting(grid))
