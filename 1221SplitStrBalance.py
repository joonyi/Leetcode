"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        R = L = 0

        for ch in s:
            if ch == 'R':
                R += 1
            else:
                L += 1

            if R == L:
                res += 1
                R = L = 0
        return res


# s = "RLRRLLRLRL" # 4
s = "RLLLLRRRLR" # 3
s = "LLLLRRRR" # 1
s = "RLRRRLLRLL" # 2
print(Solution().balancedStringSplit(s))