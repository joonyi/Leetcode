"""
Given an array nums, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?
"""

from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TLE O(nk)
        maxV = [max(nums[:k])]
        for i in range(1, len(nums) - k + 1):
            maxV.append(max(nums[i:i + k]))

        return maxV

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        winMax = []
        idx_dq = []
        for i in range(len(nums)):
            while idx_dq and idx_dq[0] < i - k + 1:  # front of dq already out of window
                idx_dq.pop(0)
            while idx_dq and nums[idx_dq[-1]] < nums[i]:
                idx_dq.pop()  # pop out index that smaller than curr i
            idx_dq.append(i)  # so that max index always at the front
            if i >= k - 1:
                winMax.append(nums[idx_dq[0]])

        return winMax

    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = nums[0]
        max_right[n - 1] = nums[n - 1]
        for i in range(1, n):
            max_left[i] = nums[i] if i % k == 0 else max(max_left[i - 1], nums[i])
            j = n - i - 1
            max_right[j] = nums[j] if j % k == 0 else max(max_right[j + 1], nums[j])

        i, j = 0, 0
        winMax = [0] * (n - k + 1)
        while i + k <= n:
            winMax[j] = max(max_left[i + k - 1], max_right[i])
            i += 1
            j += 1
        return winMax


nums, k = [1,3,-1,-3,5,3,6,7], 3  # [3,3,5,5,6,7]
# nums, k = [1,-1], 1  # [1, -1]
# nums, k = [7,2,4], 2  # [7, 4]
print(Solution().maxSlidingWindow2(nums, k))
