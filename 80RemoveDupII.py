"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the
new length.

Do not allocate extra space for another array, you must do this by modifying the input array
in-place with O(1) extra memory.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # In general, change 2 to k become remove k duplicates
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i

    def removeDuplicates2(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        i = j = cnt = 1
        while j < n:
            if nums[j] != nums[j-1]:
                cnt = 1
                nums[i] = nums[j]
                i += 1
            else:
                if cnt < 2:
                    nums[i] = nums[j]
                    i += 1
                    cnt += 1
            j += 1
        return i




nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates2(nums))