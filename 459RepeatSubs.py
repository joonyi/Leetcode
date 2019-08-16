"""
Given a non-empty string check if it can be constructed by taking a substring of it and
appending multiple copies of the substring together. You may assume the given string consists
of lowercase English letters only and its length will not exceed 10000.
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)//2 + 1):
            x = s[:i]
            y = s[i:i + len(x)]
            cnt = 1
            while y:
                if x == y:
                    cnt += 1
                    if cnt == len(s) // len(x) and cnt * len(x) == len(s):
                        return True
                    y = s[i*cnt:(i * cnt) + len(x)]
                else:
                    break

        return False

    def repeatedSubstringPattern2(self, str):
        """
        if S is composed of k substrings s, then SS = S + S should contain 2k substrings.
        Destroying the first and the last character leads to at least (2k - 2) substrings left.
        Since k >= 2 imply 2k - 2 >= k
        which means that SS[1:-1] should still contain S

        Consider a string S="helloworld". Now, given another string T="lloworldhe", can we figure out if T is a rotated version of S?
        Yes, we can! We check if S is a substring of T+T.
        """

        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1 # if str exists in ss


s = "abab" # T
# s = "aba" #F
# s = "abcabcabcabc" #T
# s = "ababab" #T
# s = "aabaaba" #F
print(Solution().repeatedSubstringPattern2(s))