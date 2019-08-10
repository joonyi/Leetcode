"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))