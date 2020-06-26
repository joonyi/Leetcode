"""
Given an integer array, you need to find one continuous subarray that if you only
sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
"""

from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Find left most and right most index of the unsorted array
        # by comparing two elements
        l, r = len(nums), 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    r = max(r, j)
                    l = min(l, i)

        if r - l < 0:  # r never moves
            return 0
        return r - l + 1

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        # Sort the arr and compare with the original arr
        # to find start and end index. O(nlgn)
        snums = sorted(nums)
        st, end = len(snums), 0
        for i in range(len(snums)):
            if snums[i] != nums[i]:
                st = min(st, i)
                end = max(end, i)

        if end - st >= 0:
            return end - st + 1
        return 0

    def findUnsortedSubarray3(self, nums: List[int]) -> int:
        """
        Determine the correct position of the minimum and the maximum element in the
        unsorted subarray to determine the boundaries of the required unsorted subarray.
        """
        st = []
        l, r = len(nums), 0
        for i in range(len(nums)):
            # keep pushing in rising slope, when falling slope occur, this element's in incorrect position
            # also keep popping out till this element is the next greater element
            while st and nums[st[-1]] > nums[i]:
                l = min(l, st.pop())
            st.append(i)
        st = []
        for i in range(len(nums) - 1, -1, -1):
            # keep pushing in falling slope, when rising slope occur, this element's in incorrect position
            # also keep popping out till this element is the next lesser element
            while st and nums[st[-1]] < nums[i]:
                r = max(r, st.pop())
            st.append(i)

        if r - l > 0:  # end at right side of start means unsorted window found
            return r - l + 1
        return 0

    def findUnsortedSubarray4(self, nums: List[int]) -> int:
        # The idea is to find the start and end of unsorted list
        _min, _max = float('inf'), float('-inf')

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:  # looking for falling slope where unsorted start
                _min = min(_min, nums[i])  # record lowest of falling slope
                _max = max(_max, nums[i - 1])  # record highest of falling slope

        l, r = 0, len(nums) - 1
        while l < len(nums):  # 1 index before _min is the start of unsorted list
            if _min < nums[l]:
                break
            l += 1

        while r >= 0:  # 1 index after _max is the end of unsorted list
            if _max > nums[r]:
                break
            r -= 1

        if r - l > 0:  # end at right side of start means unsorted window found
            return r - l + 1
        return 0


nums = [2, 6, 4, 8, 10, 9, 15]  # 5
# nums = [1,2,3,4]  # 0
# nums = [2,1]  # 2
nums = [2, 6, 4, 8, 7, 3, 15]
print(Solution().findUnsortedSubarray3(nums))
