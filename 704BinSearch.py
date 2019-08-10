"""
Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index,
otherwise return -1.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid


        return -1

# nums = [-1,0,3,5,9,12]
# target = 9
# nums = [-1,0,3,5,9,12]
# target = 2
nums = [5]
target = 5
print(Solution().search(nums, target))