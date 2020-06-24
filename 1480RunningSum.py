"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cnt = 0
        for i, n in enumerate(nums):
            cnt += n
            nums[i] = cnt
        return nums

    def runningSum2(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

    def runningSum2(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        return list(accumulate(nums))


nums = [1,2,3,4]
nums = [1,1,1,1,1]
nums = [3,1,2,10,1]
print(Solution().runningSum(nums))
