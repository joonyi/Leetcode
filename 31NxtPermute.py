"""
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order
(ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs
are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]: # Look for num left side bigger
            i -= 1

        # if such number exist find next lesser, swap then reverse
        # else proceed to swap
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        self.Reverse(nums, i + 1)

        print(nums)

    def Reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation2(self, nums):
        i = k = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        j = i
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
        if i > 0:
            i -= 1
            k = i
            while nums[k] <= nums[i]:
                k += 1
            nums[i], nums[k] = nums[k], nums[i]

        print(nums)

# nums = [1,5,8,4,7,6,5,3,1]
# nums = [1,2,3]
# nums = [1,5,1] # 511
nums = [2,3,0,2,4,1]
Solution().nextPermutation(nums)
