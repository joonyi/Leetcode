"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
"""

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.nums[i+1] = self.nums[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j+1] - self.nums[i]

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))