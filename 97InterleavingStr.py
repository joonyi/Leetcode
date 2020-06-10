"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] or \
                        dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

        return dp[m][n]

    def isInterleave2(self, s1, s2, s3):
        # See s3 as a grid, if s1 matches go left, s2 matches go down
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        queue = [(0, 0)]
        visited =  {(0, 0)}
        while queue:
            x, y = queue.pop(0)
            if x + y == l:  # reached bottom right, return True
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                queue.append((x + 1, y))  # move right
                visited.add((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                queue.append((x, y + 1))  # move down
                visited.add((x, y + 1))
        return False  # finish queue but not able to reach destination





s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"  # true

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"  # false


print(Solution().isInterleave2(s1, s2, s3))