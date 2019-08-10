"""
Given a sorted array consisting of only integers where every element appears twice
except for one element which appears once. Find this single element that appears only once.
"""


class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        single = nums[0]
        for i in range(1, len(nums)):
            single ^= nums[i]
        return single

    def singleNonDuplicate2(self, nums):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]: # if no pair, single on the left
                end = mid
            else: # else single on the right
                start = mid + 2

        return nums[start]

# Example: |0 1 1 3 3 6 6|
#               ^ ^
# Next:    |0 1 1|3 3 6 6
# Example: |1 1 3 3 5 6 6|
#               ^ ^
# Next:     1 1 3 3|5 6 6|

nums = [1,1,2,3,3,4,4,8,8]
# nums = [3,3,7,7,10,11,11]
print(Solution().singleNonDuplicate2(nums))