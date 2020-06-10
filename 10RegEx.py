"""
Given an input string (s) and a pattern (p), implement regular expression matching with support
for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch2(self, text, pattern):
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def isMatch3(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    def isMatch4(self, s, p):
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (i and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = i and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')

        return dp[m][n]

"""
dp[i][j]: i index in text, j index in pattern
state equation:
if s[i] == p[j] or p[j] == '.' => dp[i][j] = dp[i-1][j-1] 
if p[j] == '*' => dp[i][j] = dp[i][j-2] or
               => dp[i][j] = dp[i-1][j] if s[i] == p[j-1] or p[j-1] == '.'
else False

    0 1 2 3 4 5 6
      x a * b . c
0   T F F F F F F
1 x F T F T F F F
2 a F F T T F F F
3 a F F F T F F F
4 b F F F F T F F
5 y F F F F F T F
6 c F F F F F F T*
"""
# s, p = "aa", "a*" # T
s, p = "xaabyc", "xa*b.c"
print(Solution().isMatch4(s, p))
