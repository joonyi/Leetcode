"""
Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[n][m]

s, t = "rabbbit", "rabbit"
print(Solution().numDistinct(s, t))
