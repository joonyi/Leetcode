"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as
every other number in the array.

If it is, return the index of the largest element, otherwise return -1.
"""

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        for num in nums:
            if max_num < num * 2 and max_num != num:
                return -1

        return nums.index(max_num)

    # Another idea is to find first and second largest in one scan
    def dominantIndex2(self, nums):
        if len(nums) == 0: return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0

        for i, n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n

        if highest < secondHighest * 2:
            highestIndex = -1

        return highestIndex



nums = [1,2,3,4]
print(Solution().dominantIndex2(nums))