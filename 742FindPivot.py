"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the
index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes,
you should return the left-most pivot index.
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0

        forward = [0] * len(nums)
        backward = [0] * len(nums)

        for i in range(1, len(nums)):
            forward[i] = forward[i-1] + nums[i-1]
            backward[i] = backward[i-1] + nums[len(nums)-i]
        backward.reverse()
        for i in range(len(nums)):
            if forward[i] == backward[i]:
                return i
        return -1

    def pivotIndex2(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

# nums = [1, 7, 3, 6, 5, 6]
nums = [-1,-1,-1,0,1,1]
# nums = [-1,-1,-1,-1,-1,0]
print(Solution().pivotIndex(nums))
