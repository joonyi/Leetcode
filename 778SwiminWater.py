"""
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if and only if
the elevation of both squares individually are at most t. You can swim infinite distance in zero time.
Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the
bottom right square (N-1, N-1)?
"""

class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from heapq import heappush, heappop
        m, n = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visit = [[0 for _ in range(n)] for _ in range(m)]
        visit[0][0] = 1
        path = []
        T = grid[0][0]
        i, j = 0, 0
        while i != m - 1 or j != n - 1:
            node, i, j = heappop(heap)
            path.append(node)
            if node > T:
                T = node
            if j - 1 >= 0 and visit[i][j - 1] == 0:  # left
                visit[i][j - 1] = 1
                heappush(heap, (grid[i][j - 1], i, j - 1))
            if j + 1 < n and visit[i][j + 1] == 0:  # right
                visit[i][j + 1] = 1
                heappush(heap, (grid[i][j + 1], i, j + 1))
            if i - 1 >= 0 and visit[i - 1][j] == 0:  # up
                visit[i - 1][j] = 1
                heappush(heap, (grid[i - 1][j], i - 1, j))
            if i + 1 < m and visit[i + 1][j] == 0:  # down
                visit[i + 1][j] = 1
                heappush(heap, (grid[i + 1][j], i + 1, j))

        return T



# A = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
A = [[0,2],[1,3]]
# A = [[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]]
print(Solution().swimInWater(A))