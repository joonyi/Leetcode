"""
Given an array of integers nums sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            return [-1, -1]

        start, end = left, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            right = end
        else:
            right = start

        return [left, right]

    def searchRange2(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]

    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange3(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        i, j = 0, len(nums) - 1
        res = [-1, -1]
        # Search for the left one
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] != target:
            return res
        else:
            res[0] = i

        # Search for the right one
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2 + 1 # Make mid biased to the right
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid # So that this won't make the search range stuck
            res[1] = j
        return res


# Idea: binary search [start, end] for left, then binary search [left, end] for right
# Idea 2: binary search for starting index of target then starting index of target+1
# nums = [5,7,7,8,8,10]
# target = 8
# nums = [5,7,7,8,8,10]
# target = 6
nums = [1]
target = 1
print(Solution().searchRange3(nums, target))