"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pass


nums, target = [1, 0, -1, 0, -2, 2], 0
print(Solution().fourSum(nums, target))
