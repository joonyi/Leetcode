"""
Given a set of distinct positive integers, find the largest subset such that
every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.
"""
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        nums.sort()  # all divisors appear before current
        dp = [1] * n  # max divisible subset length
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

        # Get the max div and index from dp
        maxDiv = max(dp)
        maxIdx = dp.index(maxDiv)

        res = []
        prev = nums[maxIdx]
        for i in range(n - 1, -1, -1):
            # construct output that have the same divisor
            if dp[i] == maxDiv and prev % nums[i] == 0:
                res.append(nums[i])
                prev = nums[i]
                maxDiv -= 1
        return res

    def largestDivisibleSubset2(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        nums.sort()
        dp = [(0, 0)] * n  # (max divible, is divible from which index)
        dp[0] = (1, 0)
        maxIndex, maxVal = 0, 1
        for i in range(1, n):
            dp[i] = max((dp[j][0] + 1, j) for j in range(i + 1) if nums[i] % nums[j] is 0)
            if dp[i][0] > maxVal:
                maxIndex, maxVal = i, dp[i][0]
        i, lds = maxIndex, [nums[maxIndex]]
        while i != dp[i][1]:  # dp[i][1] to identify divisor of the prevrious element
            i = dp[i][1]
            lds.append(nums[i])
        return lds

    def largestDivisibleSubset3(self, nums: List[int]) -> List[int]:
        if len(nums) == 0: return []
        nums.sort()
        sol = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                # update when remainder is zero and len of solution becomes greater
                if nums[i] % nums[j] == 0 and len(sol[i]) < len(sol[j]) + 1:
                    sol[i] = sol[j] + [nums[i]]
        return max(sol, key=len)


# nums = [1,2,3]  # [1,2] or [1,3]
nums = [1,2,4,8]
# nums = [2,3,4,8]  # [8,4,2]
# nums = [2,3,4,9,8]  # [2,4,8]
nums = [4,8,10,240]  # [4,8,240]
print(Solution().largestDivisibleSubset3(nums))

