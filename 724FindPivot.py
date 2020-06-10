"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index
is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes,
you should return the left-most pivot index.
"""

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

nums = [1, 7, 3, 6, 5, 6]
# nums = [1, 2, 3]
print(Solution().pivotIndex(nums))