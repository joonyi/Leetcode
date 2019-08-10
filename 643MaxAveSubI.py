"""
Given an array consisting of n integers, find the contiguous subarray of given length k
that has the maximum average value. And you need to output the maximum average value.
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # sliding window
        if not nums: return nums
        if len(nums) == 1: return nums[0]
        val = max_val = sum(nums[:k])
        for i in range(1, len(nums) - k + 1):
            val = val - nums[i-1] + nums[i+k-1]
            if val > max_val:
                max_val = val

        return max_val/k

    def findMaxAverage2(self, nums, k):
        # Prefix sum
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        ma = P[k]
        for i in range(len(nums) - k + 1):
            ma = max(ma, P[i + k] - P[i])

        return ma / float(k)


nums, k = [1,12,-5,-6,50,3], 4
print(Solution().findMaxAverage2(nums, k))