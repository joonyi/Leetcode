"""
Given an array with n objects colored red, white or blue, sort them in-place so that
objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, len(nums) - 1
        while i <= k:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            elif nums[i] == 2:
                ## move one step back since nums[i] has been replaced by nums[k]
                ## need to double check
                nums[i], nums[k] = nums[k], nums[i]
                i -= 1
                k -= 1
            i += 1

    def sortColors2(self, nums):
        n0, n1, n2 = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
                n2 += 1
                n1 += 1
                n0 += 1
            elif nums[i] == 1:
                nums[n2] = 2
                nums[n1] = 1
                n2 += 1
                n1 += 1
            elif nums[i] == 2:
                nums[n2] = 2
                n2 += 1

    def sortColors3(self, nums):
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] == 1:
                j += 1
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1

# This is Dutch national flag problem
# three-way partitioning to arrange the numbers so that those larger than the pivot come first,
# then those equal to the pivot come next, and then those smaller than the pivot come last.
nums = [2,0,2,1,1,0]
print(Solution().sortColors3(nums))