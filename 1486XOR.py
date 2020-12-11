"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = start
        for i in range(1, n):
            num = start + 2*i
            res ^= num

        return res


n = 5
start = 0 # 8
n = 4
start = 3 # 8
n, start = 1, 7 # 7
n, start = 10, 5 # 2
print(Solution().xorOperation(n, start))