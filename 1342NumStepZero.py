"""
Given a non-negative integer num, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            cnt += 1
        return cnt

    def numberOfSteps2(self, num: int) -> int:
        if num == 0: return 0
        res = 0
        while num:
            if num & 1:
                res += 2  # +2 bcs first substract then divide
            else:
                res += 1  # Do divide
            num >>= 1
        return res - 1  # when num is 1 just substract no divide


num = 14  # 6
# num = 8  # 4
num = 123  # 12
print(Solution().numberOfSteps2(num))
