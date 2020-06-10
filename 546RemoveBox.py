"""
Given several boxes with different colors represented by different positive numbers.
You may experience several rounds to remove boxes until there is no box left.
Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1),
remove them and get k*k points.
Find the maximum points you can get.
"""


class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        N = len(boxes)
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and boxes[m + 1] == boxes[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i + 1, j, 0) + (k + 1) ** 2
                for m in range(i + 1, j + 1):
                    if boxes[i] == boxes[m]:
                        ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        # dp(i,j,k) means the max points you can earn between boxes "i" and "j",
        # with "k" boxes before i that has the same color as "i".
        return dp(0, N - 1, 0)

    def removeBoxes2(self, boxes):
        N = len(boxes)
        dp = [[[0] * N for _ in range(N)] for _ in range(N)]
        for j in range(N):
            for k in range(j + 1):
                dp[j][j][k] = (k + 1) * (k + 1)

        for l in range(1, N):
            for j in range(l, N):
                i = j - l
                for k in range(i + 1):
                    res = (k + 1) * (k + 1) + dp[i + 1][j][0]

                    for m in range(i + 1, j + 1):
                        if boxes[m] == boxes[i]:
                            res = max(res, dp[i + 1][m - 1][0] + dp[m][j][k + 1])
                    dp[i][j][k] = res

        if N == 0:
            return 0
        else:
            return dp[0][N - 1][0]



boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
print(Solution().removeBoxes(boxes))