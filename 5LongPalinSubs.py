"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '' or len(s) < 1:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1)//2
                end = i + length//2

        return s[start:end+1]

    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome2(self, s):
        n = len(s)
        res = ''
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j] and (res == None or j - i + 1 > len(res)):
                    res = s[i:j+1]

        return res

    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring
    def longestPalindrome3(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


s = 'character'
print(Solution().longestPalindrome3(s))