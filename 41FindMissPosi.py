"""
Given an unsorted integer array, find the smallest missing positive integer.
"""
import sys
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass

    def firstMissingPositive2(self, nums):
        if not nums:
            return 1
        nums = list(set(nums))
        ret = len(nums)
        i = len(nums) - 1
        while i >= 0:
            while nums[i] != i + 1 and (0 < nums[i] <= len(nums)):
                swap = nums[i] - 1
                nums[i], nums[swap] = nums[swap], nums[i]
            if not (0 < nums[i] <= len(nums)):
                ret = i
            i -= 1
        return ret + 1

    def firstMissingPositive3(self, nums):
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                swap = nums[i] - 1
                nums[i], nums[swap] = nums[swap], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

nums = [1,2,0]
print(Solution().firstMissingPositive3(nums))