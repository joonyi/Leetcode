"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Note:
You can assume that you can always reach the last inde
"""

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        # TLE
        n = len(nums)
        f = [2**32-1] * n
        f[n - 1] = 0
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j <= i + nums[i] and j < n:
                f[i] = min(f[i], 1 + f[j])
                j += 1

        return f[0]

    def jump2(self, nums: List[int]) -> int:
        # Look for max reachable index from each entry
        # Any element after the span of first step is second step
        if len(nums) == 1:
            return 0
        n = len(nums)
        maxIdx = nums[0]
        step = 1
        lim = nums[0]
        for i in range(1, n):
            if i > lim:
                step += 1
                lim = maxIdx
            maxIdx = max(maxIdx, i + nums[i])

        return step


nums = [2,3,1,1,4]  # 2
nums = [2,3,0,1,4]  # 2
nums = [0]  # 0
print(Solution().jump2(nums))

