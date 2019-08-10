class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p, q = 0, 0
        test = ''
        while p < len(s) and q < len(t):
            if s[p] == t[q]:
                test += t[q]
                p += 1
                q += 1
            else:
                q += 1

        if p == len(s):
            return True
        else:
            return False


# s = "abc"
# t = "ahbgdc"
s = "axc"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))