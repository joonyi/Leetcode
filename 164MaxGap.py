"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        nums.sort()
        gap = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] > gap:
                gap = nums[i] - nums[i-1]
        return gap

    def maximumGap2(self, nums):
        from math import ceil
        if len(nums) < 2:
            return 0
        _min = min(nums)
        _max = max(nums)
        gap = ceil((_max - _min) / (len(nums) - 1))
        bucketMin = [float('inf')] * (len(nums) - 1)
        bucketMax = [float('-inf')] * (len(nums) - 1)
        for n in nums:
            if n == _min or n == _max:
                continue
            i = (n - _min) // gap
            bucketMin[i] = min(n, bucketMin[i])
            bucketMax[i] = max(n, bucketMax[i])

        gap = 0
        prev = _min
        for i in range(len(bucketMin)):
            if bucketMin[i] == float('inf') and bucketMax[i] == float('-inf'):
                continue  # empty bucket
            gap = max(gap, bucketMin[i] - prev)
            prev = bucketMax[i]

        gap = max(gap, _max - prev)
        return gap


nums = [3,6,9,1]
# nums = [10]
nums = [43, 49, 29,37,3,9,21,25]
print(Solution().maximumGap2(nums))