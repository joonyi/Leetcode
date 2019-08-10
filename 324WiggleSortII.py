"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        median = sorted(nums)[len(nums)//2] # Find median
        n = len(nums)
        left, i, right = 0, 0, n-1

        def newIndex(index, n):
            # Original Indices:    0  1  2  3  4  5  6  7  8  9 10 11
            # Mapped Indices:      1  3  5  7  9 11  0  2  4  6  8 10
            # this function will achieve this
            return (1 + 2 * index) % (n | 1)

        while i <= right: # divide into three partition lower, higher and equal to median
            if nums[newIndex(i, n)] > median:
                nums[newIndex(left, n)], nums[newIndex(i, n)] = nums[newIndex(i, n)], nums[newIndex(left, n)]
                left += 1
                i += 1
            elif nums[newIndex(i, n)] < median:
                nums[newIndex(right, n)], nums[newIndex(i, n)] = nums[newIndex(i, n)], nums[newIndex(right, n)]
                right -= 1
            else:
                i += 1


    def wiggleSort2(self, nums):
        # Don't understand
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]


    def wiggleSort3(self, nums):
        n = len(nums)
        A = sorted(nums)
        i = (n - 1) // 2
        j = n - 1
        toggle = 0
        for k in range(n):
            if toggle == 0:
                nums[k] = A[i]
                i -= 1
            else:
                nums[k] = A[j]
                j -= 1
            toggle ^= 1 # toggle btw i and j


    def wiggleSort4(self, nums):
        """
        Just put sorted numbers in array
        Put largest numbers in odd indexes first
        Then put remaining numbers in even indexes
        So even < odd > even
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop()
        for i in range(0, len(nums), 2): nums[i] = arr.pop()

nums = [1, 5, 1, 1, 6, 4]
# nums = [1, 3, 2, 2, 3, 1]
print(Solution().wiggleSort4(nums))