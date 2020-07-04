"""
Given a string s, the power of the string is the maximum length of a non-empty substring
that contains only one unique character.

Return the power of the string.
"""


class Solution:
    def maxPower(self, s: str) -> int:
        i, j = 0, 1
        power = 1
        while j < len(s):
            if s[i] != s[j]:
                i = j
                j += 1
            else:
                j += 1
            power = max(power, j - i)

        return power

    def maxPower2(self, s: str) -> int:
        power = cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                cnt = 1
            power = max(power, cnt)
        return power


# s = "leetcode"  # 2
s = "abbcccddddeeeeedcba"  # 5
# s = "triplepillooooow"  # 5
# s = "hooraaaaaaaaaaay"  # 11
# s = "tourist"  # 1
# s = "ccbccbb"  # 2
print(Solution().maxPower2(s))
