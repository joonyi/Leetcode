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

    def lengthOfLIS2(self, nums):
        import bisect
        # Although the elements are not correct, but the length is correct
        a = []
        for num in nums:
            i = bisect.bisect_left(a, num)  # the return index partition left < num, right >= num
            if i == len(a):  # new index bigger than the rightmost num
                a.append(num)
            else:
                a[i] = num  # element has been changed, but the sub's length has not changed.

        return len(a)

nums = [10,9,2,5,3,7,101,18]
nums = [8, 2, 5, 1, 6, 7, 9, 3]
print(Solution().lengthOfLIS2(nums))