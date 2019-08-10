"""
Give a string s, count the number of non-empty (contiguous) substrings that
have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings
are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # TLE
        from math import log2
        n = (int(log2(len(s))) + 1) * 2
        bin_str = [0] * n
        j = 0
        for i in range(n//2):
            bin_str[j] = "0"*(i + 1) + "1"*(i + 1)
            bin_str[j+1] = "1" * (i + 1) + "0" * (i + 1)
            j += 2

        cnt = 0
        for subs in bin_str:
            p, q = 0, len(subs)
            while q < len(s) + 1:
                if subs == s[p:q]:
                    cnt += 1
                p += 1
                q += 1

        return cnt

    def countBinarySubstrings2(self, s):
        groups = [1] # element represents how many consecutive '0' or '1'
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            # useful property, "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")
            ans += min(groups[i - 1], groups[i])
        return ans

    def countBinarySubstrings3(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)


# s = "00110011"
# s = "10101"
# s = "00110"
s = "1011110000"
print(Solution().countBinarySubstrings3(s))