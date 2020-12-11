"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.
"""

from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = dict()
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1

        res = 0
        for k, v in cnt.items():
            if v >= 2:
                res += v * (v-1) // 2

        return res



nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
# nums = [1,2,3]

print(Solution().numIdenticalPairs(nums))

