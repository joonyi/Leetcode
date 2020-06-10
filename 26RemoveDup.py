"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array
in-place with O(1) extra memory.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 1 or n != nums[i - 1]:
                nums[i] = n
                i += 1
        return i

nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))