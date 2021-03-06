"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer,
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n
as large as possible.
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]

        return sum
# Idea: Minimum element gets add into the result in sacrifice of maximum element.
nums = [1,4,3,2]
print(Solution().arrayPairSum(nums))
