"""
Given a non-empty integer array, find the minimum number of moves required to make all
array elements equal, where a move is incrementing a selected element by 1 or decrementing
a selected element by 1.

You may assume the array's length is at most 10,000.
"""

from typing import List
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        cnt = 0
        while i < j:
            cnt += nums[j] - nums[i]
            i += 1
            j -= 1
        return cnt

    def minMoves22(self, nums):
        median = sorted(nums)[len(nums) // 2]
        return sum(abs(num - median) for num in nums)


nums = [1,2,3]  # 2
nums = [1,2,3,4]  # 4
print(Solution().minMoves2(nums))
