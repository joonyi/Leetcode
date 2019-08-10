"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # TLE
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        self.res = []
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(m):
            for j in range(n):
                path = []
                visited = [[0 for _ in range(n)] for _ in range(m)]
                self.dfs(matrix, visited, i, j, path)

        return len(self.res)

    def dfs(self, matrix, visited, i, j, path):
        visited[i][j] = 1
        path.append(matrix[i][j])
        if len(path) > len(self.res):
            self.res = path[:]
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and visited[x][y] == 0 and matrix[i][j] > matrix[x][y]:
                self.dfs(matrix, visited, x, y, path)
                path.pop()
                visited[x][y] = 0

    def longestIncreasingPath2(self, matrix):
        # Why complex number can be used here
        matrix = {i + j * 1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        length = {}
        for z in sorted(matrix, key=matrix.get):
            length[z] = 1 + max([length[Z]
                                 for Z in (z + 1, z - 1, z + 1j, z - 1j)
                                 if Z in matrix and matrix[z] > matrix[Z]]
                                or [0])
        return max(length.values() or [0])

    def longestIncreasingPath3(self, matrix):
        # Use dp to record previous results and choose the max dp value of smaller neighbors.
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))

class Solution2(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # Find length of longest increasing path
        # From each cell, move to four directions: up, down, left, right
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        max_path = 1
        for i in range(m):
            for j in range(n):
                # get a current (local max) path by visiting matrix[i][j] and its neighbors
                curr_path = self.dfs(matrix, i, j, cache)
                max_path = max(max_path, curr_path)

        return max_path

    def dfs(self, matrix, i, j, cache):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if cache[i][j] != 0:
            return cache[i][j]

        max_path = 1
        for d in dirs:
            x, y = i + d[0], j + d[1]
            # if the new i, j cell is less than or equal to the current, don't consider it
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= matrix[i][j]:
                continue

            curr_path = 1 + self.dfs(matrix, x, y, cache)
            max_path = max(max_path, curr_path)

        cache[i][j] = max_path
        return max_path



# matrix = [[9,9,4],
#           [6,6,8],
#           [2,1,1]]
matrix = [[7,8,9],[9,7,6],[7,2,3]]
print(Solution2().longestIncreasingPath(matrix))