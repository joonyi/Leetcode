"""
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1]
in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle,
the value of that triangle is the product of the labels of the vertices,
and the total score of the triangulation is the sum of these values over all N-2 triangles
in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.
"""

from typing import List
class Solution:
    def minScoreTriangulation(self, A):
        def dfs(left, right):
            if right - left + 1 < 3:
                return 0
            minN = float("inf")
            for k in range(left + 1, right):
                minN = min(minN, A[left] * A[right] * A[k] + dfs(left, k) + dfs(k, right))
            return minN

        return dfs(0, len(A) - 1)

    def minScoreTriangulation2(self, A):
        """
        • Fix one side of the polygon i, j and move k within (i, j).
        • Calculate score of the i, k, j "orange" triangle.
        • Add the score of the "green" polygon i, k using recursion.
        • Add the score of the "blue" polygon k, j using recursion.
        • Use memoization to remember minimum scores for each sub-polygons.
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                # when i, j differs less than 2 => []
                # Supply [0] so that [] or [0] evaluate into [0] and min([0]) return 0
                memo[i, j] = min([dp(i, k) + dp(k, j) + A[i] * A[j] * A[k] for k in range(i + 1, j)] or [0])
            return memo[i, j]

        return dp(0, len(A) - 1)

    def minScoreTriangulation3(self, A: List[int]) -> int:
        N = len(A)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        for d in range(2, N):
            for i in range(N - d):
                j = i + d
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k])

        return dp[0][N - 1]


"""
1. Recursive solution
2. Memoize the recursive solution (top-down)
3. Subproblem Order for DP (bottom-up)
"""
# A = [1,2,3]  # 6
A = [3,7,4,5]  # 144
# A = [1,3,1,4,1,5]  # 13
# A = [3,4,4,4]  # 96
print(Solution().minScoreTriangulation(A))
