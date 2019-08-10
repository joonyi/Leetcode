"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # TLE
        # Build new s basket each time
        s_basket = {}
        p_basket = {}

        for ch in p:
            p_basket[ch] = p_basket.get(ch, 0) + 1

        res = []
        for i in range(0, len(s)-len(p)+1):
            for ch in range(i, i+len(p)):
                s_basket[s[ch]] = s_basket.get(s[ch], 0) + 1
            if s_basket == p_basket:
                res.append(i)
            s_basket = {}

        return res

    def findAnagrams2(self, s, p):
        # Don't build s_basket each time
        # Remove one char and add one char
        if not s or not p: return ""
        if len(s) < len(p): return ""
        s_basket = {}
        p_basket = {}
        for ch in p:
            p_basket[ch] = p_basket.get(ch, 0) + 1
        for c in range(len(p)):
            s_basket[s[c]] = s_basket.get(s[c], 0) + 1
        res = []
        if s_basket == p_basket:
            res.append(0)

        for i in range(1, len(s) - len(p) + 1):
            s_basket[s[i-1]] -= 1
            if s_basket[s[i-1]] == 0:
                del s_basket[s[i-1]]
            s_basket[s[i+len(p)-1]] = s_basket.get(s[i+len(p)-1], 0) + 1
            if s_basket == p_basket:
                res.append(i)

        return res

    def findAnagrams3(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0] * 123, [0] * 123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m - 1]:
            shash[ord(x)] += 1
        for i in range(m - 1, n):
            shash[ord(s[i])] += 1
            if i - m >= 0:
                shash[ord(s[i - m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

s = "cbaebabacd"
p = "abc"
# s = "abab"
# p = "ab"
# s = "aaaaaaaaaa"
# p = "aaaaaaaaaaaaa"

print(Solution().findAnagrams3(s, p))