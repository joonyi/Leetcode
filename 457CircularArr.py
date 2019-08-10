"""
You are given a circular array nums of positive and negative integers.
If a number k at an index is positive, then move forward k steps.
Conversely, if it's negative (-k), move backward k steps. Since the array is circular,
you may assume that the last element's next element is the first element, and the
first element's previous element is the last element.

Determine if there is a loop (or a cycle) in nums. A cycle must start and end at the same index
and the cycle's length > 1. Furthermore, movements in a cycle must all follow a single direction.
In other words, a cycle must not consist of both forward and backward movements.
"""
class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return False

        n = len(nums)
        for i in range(n):
            if type(nums[i]) != int:  # visited element
                continue
            if nums[i] % n == 0:  # self-loop
                continue

            direction = (nums[i] > 0)  # loop direction, cannot be changed midway

            mark = str(i)
            while (type(nums[i]) == int) and (direction ^ (nums[i] < 0)) and (nums[i] % n != 0):
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % n

            if nums[i] == mark:
                return True

        return False


nums = [2,-1,1,2,2] # T
# nums = [-1,2] # F
# nums =  [-2,1,-1,-2,-2] # F
# nums = [-1,-2,-3,-4,-5] # F
print(Solution().circularArrayLoop(nums))