"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return True

            # At this point, cannot determine if start to mid is sorted
            # Have to move the pointer till start and mid is not duplicates
            while start < mid and nums[start] == nums[mid]:
                start += 1

            # from start to mid is sorted array
            if nums[start] < nums[mid]:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            # from start to mid is not sorted array
            else:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target or nums[end] == target:
            return True
        else:
            return False


    def search2(self, nums, target):
        for num in nums:
            if num == target:
                return True
        return False


nums, target = [2,5,6,0,0,1,2], 0  # T
# nums, target = [2,5,6,0,0,1,2], 3  # F
# nums, target = [], 5
# nums, target = [1,1,3,1], 3
nums, target = [1,3,1,1,1], 3  # T
print(Solution().search(nums, target))

