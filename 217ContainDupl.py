"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least
twice in the array, and it should return false if every element is distinct.
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

    def containsDuplicate2(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

    # hash
    def containsDuplicate3(self, nums):
        hasht = {}
        for num in nums:
            if num not in hasht:
                hasht[num] = True
            else:
                return True
        return False

nums = [1,1,1,3,3,4,3,2,4,2]
print(Solution().containsDuplicate3(nums))
