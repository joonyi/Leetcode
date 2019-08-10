"""
In a given 2D binary array A, there are two islands.
(An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.
(It is guaranteed that the answer is at least 1.)
"""
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        found = False
        queue = []
        level = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and not found:
                    self.dfs(A, i, j)
                    found = True

                if found and A[i][j] == 1:
                    queue.append((i,j))

        directions = ((0,1),(0,-1),(-1,0),(1,0))
        while queue:
            for s in range(len(queue)):
                pos = queue.pop(0)
                for d in directions:
                    x = pos[0] + d[0]
                    y = pos[1] + d[1]
                    if x < 0 or x >= len(A) or y < 0 or y >= len(A[0]):
                        continue
                    if A[x][y] == 2:
                        return level
                    elif A[x][y] == 1:
                        continue
                    elif A[x][y] == 0:
                        A[x][y] = 1
                        queue.append((x,y))
            level += 1

        return -1

    def dfs(self, A, i, j):
        A[i][j] = 2
        if (i-1 >= 0 and A[i-1][j] == 1):
            self.dfs(A, i-1, j)
        if (i+1 < len(A) and A[i+1][j] == 1):
            self.dfs(A, i+1, j)
        if (j-1 >= 0 and A[i][j-1] == 1):
            self.dfs(A, i, j-1)
        if (j+1 < len(A[0]) and A[i][j+1] == 1):
            self.dfs(A, i, j+1)

input = [[0,1],[1,0]]
input2 = [[0,1,0],[0,0,0],[0,0,1]]
input3 = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]

print(Solution().shortestBridge(input2))

