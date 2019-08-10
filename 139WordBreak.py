"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        f = [False for _ in range(len(s) + 1)]
        f[0] = True
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break

        return f[-1]

    def wordBreak2(self, s, wordDict):
        dp = [False] * (len(s) + 1)  # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j + 1] in wordDict:
                    dp[j+1] = True

        return dp

    def wordBreak3(self, s, wordDict):
        def canBreak(s, m, wordDict):
            if s in m: return m[s]
            if s in wordDict:
                m[s] = True
                return True

            for i in range(1, len(s)):
                r = s[i:]
                if r in wordDict and canBreak(s[0:i], m, wordDict):
                    m[s] = True
                    return True

            m[s] = False
            return False

        return canBreak(s, {}, set(wordDict))

# s, wordDict = "leetcode", ["leet", "code"]
# s, wordDict = "applepenapple", ["apple", "pen"]
# s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
s, wordDict = 'aaaaaaa', ["aaaa","aaa"]

print(Solution().wordBreak3(s, wordDict))