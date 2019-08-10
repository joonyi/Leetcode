from UnionFind import UnionFind
class Solution(object):
    # Iterate through each of the cell and if it is an island,
    # do dfs to mark all adjacent islands, then increase the counter by 1.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

    def numIslands2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        uf = UnionFind(grid)

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if x >= 0 and x < m and y >= 0 and y < n and  grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y) # convert matrix index to list index and union them
        return uf.count

grid = ['11110',
'11010',
'11000',
'00000']
grid2 = ['11000',
'11000',
'00100',
'00011']
grid3 = ['1011011']
grid4 = [["1","1","1","1","0"],["1","1","0","1","0"],
 ["1","1","0","0","0"],["0","0","0","0","0"]]
grid5 = [["0","1","0"],["1","0","1"],["0","1","0"]]
grid6 = [["1","1","1"],["0","1","0"],["1","1","1"]]

print(Solution().numIslands2(grid6))