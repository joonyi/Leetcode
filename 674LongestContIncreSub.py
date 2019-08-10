"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence
(subarray).
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] += dp[i-1]

        return max(dp)

# nums = [1,3,5,4,7]
nums = [2,2,2,2,2]
print(Solution().findLengthOfLCIS(nums))