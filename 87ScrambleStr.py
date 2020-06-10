"""
Given a string s1, we may represent it as a binary tree by partitioning it to
two non-empty substrings recursively.
"""

class Solution(object):
    def __init__(self):
        self.dic = {}

    def isScramble(self, s1, s2):
        if (s1, s2) in self.dic:
            return self.dic[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):  # prunning
            self.dic[(s1, s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1, s2)] = True
            return True
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        self.dic[(s1, s2)] = False
        return False

    def isScramble2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True

        n = len(s1)
        count = [0] * 26
        for i in range(n):
            count[ord(s1[i])- 97] += 1
            count[ord(s2[i]) - 97] -= 1

        if any(count):
            return False

        for i in range(1, n):
            if self.isScramble2(s1[:i], s2[:i]) and self.isScramble2(s1[i:], s2[i:]):
                return True
            if self.isScramble2(s1[:i], s2[n-i:]) and self.isScramble2(s1[i:], s2[:n-i]):
                return True

        return False

s1 = "great"
s2 = "rgeat"  # True
# s1 = "abcde"
# s2 = "caebd"  # False
print(Solution().isScramble2(s1, s2))
