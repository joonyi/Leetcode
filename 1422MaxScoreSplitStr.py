"""
Given a string s of zeros and ones, return the maximum score after splitting the string into
two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus
the number of ones in the right substring.
"""


class Solution:
    def maxScore(self, s: str) -> int:
        s = list(map(int, s))
        zeroes = [0] * len(s)
        ones = [0] * len(s)
        for i in range(1, len(s)):
            if s[i - 1] == 0:
                zeroes[i] += zeroes[i - 1] + 1
            else:
                zeroes[i] = zeroes[i - 1]

            if s[len(s) - i] == 1:
                ones[i] += ones[i - 1] + 1
            else:
                ones[i] = ones[i - 1]

        cnt = 0
        for i in range(1, len(s)):
            cnt = max(cnt, zeroes[i] + ones[len(s) - i])

        return cnt


    def maxScore2(self, s: str) -> int:
        """
        Result = Max of (ZerosOnLeft + OnesOnRight)
        = Max of (ZerosOnLeft + (TotalOnes - OnesOnLeft))
        = Max of (ZerosOnLeft - OnesOnLeft) + TotalOnes (as TotalOnes is constant)
        """
        zeros, ones = 0, 0
        _max = float('-inf')
        for i in range(len(s)):
            if s[i] == "0":
                zeros += 1
            else:
                ones += 1
            if i != len(s) - 1:
                _max = max(_max, zeros - ones)
        return _max + ones


s = "011101"  # 5
# s = "00111"  # 5
s = "1111"  # 3
# s = ""
# s = "01"
print(Solution().maxScore2(s))
