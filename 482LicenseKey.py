"""
You are given a license key represented as a string S which consists only alphanumeric character
and dashes. The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such that each group contains exactly
K characters, except for the first group which could be shorter than K, but still must contain
at least one character. Furthermore, there must be a dash inserted between two groups and
all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the rules described above.
"""
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.upper().split('-'))
        div, rem = divmod(len(S), K)
        res = ''

        if rem:
            res += S[:rem] + '-'

        i = rem
        for _ in range(div):
            res += S[i:i+K] + '-'
            i += K

        return res[:-1]

    def licenseKeyFormatting2(self, S, K):
        S = S.replace("-", "").upper()[::-1] # Reverse it so that K block is added until remainder
        return '-'.join(S[i:i + K] for i in range(0, len(S), K))[::-1]

# Speed: List comprehension > build a list then join > string concatenation
S, K = "5F3Z-2e-9-w", 4
# S, K = "2-5g-3-J", 2
# S, K = "2-4A0r7-4k", 3
print(Solution().licenseKeyFormatting2(S, K))