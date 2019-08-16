"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # TLE
        def search(s):
            for j in range(len(s)):
                if 1 <= int(s[:j+1]) <= 26:
                    ch.append(s[:j+1])
                else:
                    return

                search(s[j+1:])

                if len(''.join(ch)) == self.length:
                    self.cnt += 1

                if len(''.join(ch)) != 0:
                    ch.pop()

        ch = []
        self.cnt = 0
        self.length = len(s)
        search(s)
        return self.cnt

    def numDecodings2(self, s):
        if s == "": return 0
        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if s[i-1] != "0": # check for 1~9
                dp[i] += dp[i-1]
            if i != 1 and "09" < s[i-2:i] < "27": # check for 10~26
                dp[i] += dp[i-2]
        return dp[len(s)]

    def numDecodings3(self, s):
        def search(s, memo):
            if s in memo: # if already in memo, return it
                return memo[s]
            if len(s) <= 1: # if not in memo, one digit and two digit return one, except '0'
                return 1 if s != "0" else 0
            res, n, i = 0, len(s), 1
            while i <= n and 1 <= int(s[:i]) <= 26:
                res += search(s[i:], memo)
                i += 1
            memo[s] = res
            return res

        if s == "":
            return 0

        return search(s, {})

    def numDecodings4(self, s):
        def dfs(word, memo):
            if len(word) == 0:
                return 1
            if word[0] == "0":
                return 0
            if word not in memo:
                Numways = 0
                if len(word) >= 2 and int(word[0:2]) <= 26:
                    Numways += dfs(word[2:], memo)
                Numways += dfs(word[1:], memo)
                memo[word] = Numways
            return memo[word]
        return dfs(s, {})

# s = "12"
s = "226" # 3
# s = "01"
# s = "4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948"
print(Solution().numDecodings4(s))


