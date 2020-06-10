"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only
1's and return its area.
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # 2D dp
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        maxsqlen = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    maxsqlen = max(maxsqlen, dp[i][j]) # max of an entry in dp
        return maxsqlen * maxsqlen

    def maximalSquare2(self, matrix):
        # 1D dp. Can simplify bcs previous approach of calculating dp of i row,
        # using only previous element and i-1 row
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        dp = [0 for _ in range(n + 1)]
        maxsqlen, prev = 0, 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    # dp[j] = min(min(dp[j-1], prev), dp[j]) + 1
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return maxsqlen * maxsqlen


matrix = [['1','0','1','0','0'],
          ['1','0','1','1','1'],
          ['1','1','1','1','1'],
          ['1','0','0','1','0']]
print(Solution().maximalSquare2(matrix))