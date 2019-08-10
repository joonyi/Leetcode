"""
Given an array of n positive integers and a positive integer s, find the minimal length
of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = float('inf')
        left = 0
        sum = 0
        for i in range(n):
            sum += nums[i]
            while sum >= s:
                res = min(res, i + 1 - left)
                sum -= nums[left]
                left += 1

        if res != float('inf'):
            return res
        else:
            return 0

    def minSubArrayLen2(self, s, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1): # convert to cumulative array
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= s:
                left = self.find_left(left, right, nums, s, n) # Use binary search for left that make sum larger than s
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left


s = 7
nums = [2,3,1,2,4,3]
print(Solution().minSubArrayLen2(s, nums))