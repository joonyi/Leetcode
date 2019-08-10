"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching
with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        s_cur = 0
        p_cur = 0
        match = 0
        star = -1
        # Scan through s
        while s_cur < len(s):
            # if two pointers match or p is '?', move two pointers
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur += 1
                p_cur += 1
            # when '*' found, set match and star position
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur += 1
            # when p pointer at star, always keep p one behind star
            # and move s pointer according to match
            elif (star != -1):
                p_cur = star + 1
                match += 1
                s_cur = match
            else:
                return False

        # Scan through p
        # if the rest of p is '*', move the pointer to the end
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur += 1

        if p_cur == len(p):
            return True
        else:
            return False

    # dp[n] represents if substring s[:n] match the pattern
    def isMatch2(self, s, p):
        length = len(s)

        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

    def isMatch3(self, s, p):
        m = len(s)
        n = len(p)
        cur = [False] * (m + 1)
        cur[0] = True
        for j in range(1, n+1):
            pre = cur[0]
            cur[0] = cur[0] and p[j-1] == "*"
            for i in range(1, m+1):
                temp = cur[i]
                if p[j-1] != "*":
                    cur[i] = pre and (s[i-1] == p[j-1] or p[j-1] == '?')
                else:
                    cur[i] = cur[i-1] or cur[i]
                pre = temp
        return cur[m]

s = "adceb"
p = "*a*b"
print(Solution().isMatch3(s,p))