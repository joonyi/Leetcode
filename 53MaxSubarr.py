"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert it into cumulative list. Do it when element is non-negative
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

    def maxSubArray2(self, nums):
        maxSoFar = nums[0]
        maxEndHere = nums[0]
        for i in range(1, len(nums)):
            maxEndHere = max(maxEndHere + nums[i], nums[i])
            maxSoFar = max(maxSoFar, maxEndHere)
        return maxSoFar

nums = [-2,1,-3,4,-1,2,1,-5,4] # 6
print(Solution().maxSubArray2(nums))