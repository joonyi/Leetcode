"""
Given two words word1 and word2, find the minimum number of steps required to make
word1 and word2 the same, where in each step you can delete one character in either string.
"""

class Solution(object):
    def minDistance(self, word1, word2):
        # 2D dp
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 1D dp
        dp = [0] * (len(word2) + 1)
        for i in range(len(word1) + 1):
            tmp = [0] * (len(word2) + 1)
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    tmp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    tmp[j] = dp[j - 1]
                else:
                    tmp[j] = 1 + min(dp[j], tmp[j - 1])
            dp = tmp

        return dp

    """
    Let dp(i, j) be the answer for strings A[i:] and B[j:]. Let's try to compute it by a top-down dp:

    When i == len(A) or j == len(B), one of the strings is empty, so the answer is just the sum of the remaining lengths.
    When A[i] == B[j], the answer is just dp(i+1, j+1). For example, when evaluating the distance between "acai" and "apple", we only need to look at the distance between "cai" and "pple".
    When A[i] != B[j], then they both cannot be in the final word, so we either delete A[i] or B[j]. Thus, our answer is 1 + min(dp(i+1, j), dp(i, j+1)).
    """
    def minDistance3(self, A, B):
        # Top down dp
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if i == len(A) or j == len(B):
                    ans = len(A) + len(B) - i - j
                elif A[i] == B[j]:
                    ans = dp(i + 1, j + 1)
                else:
                    ans = 1 + min(dp(i + 1, j), dp(i, j + 1))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

word1, word2 = "sea", "eat"
print(Solution().minDistance3(word1, word2))