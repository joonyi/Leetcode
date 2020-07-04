"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that
j != i and nums[j] < nums[i].

Return the answer in an array.
"""
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    cnt[i] += 1

        return cnt

    def smallerNumbersThanCurrent2(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        res = [0] * len(nums)
        for i in range(len(nums)):
            cnt[nums[i]] += 1
        for i in range(1, 101):
            cnt[i] += cnt[i - 1]
        for i in range(len(nums)):
            if nums[i] == 0:
                res[i] = 0
            else:
                res[i] = cnt[nums[i] - 1]
        return res


# Another idea is to sort the array and get information from the index
nums = [8,1,2,2,3]  # [4,0,1,1,3]
# nums = [6, 5, 4, 8]  # [2,1,0,3]
# nums = [7, 7, 7, 7]  # [0,0,0,0]
print(Solution().smallerNumbersThanCurrent2(nums))