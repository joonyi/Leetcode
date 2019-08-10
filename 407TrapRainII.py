class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        if len(heightMap) == 1: return 0
        for row in heightMap:
            if len(row) == 2: return 0

        def dfs(heightMap, i, j):
            if j < n or i < m:
                if M[i][j]
                dfs(heightMap, i + 1, j)
                dfs(heightMap, i, j + 1)


        m, n = len(heightMap), len(heightMap[0])
        self.volume = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                dfs(heightMap, i, j)








heightMap = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
print(Solution().trapRainWater(heightMap))