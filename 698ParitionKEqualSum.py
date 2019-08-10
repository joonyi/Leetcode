"""
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Not working
        total = sum(nums)
        if total % k != 0: return False
        if len(nums) == 1 and k != 1: return False

        equal_sum = total // 4
        i, j = 0, len(nums)
        cnt, tmp = 0, 0
        while i < j:
            tmp += nums[i]
            if tmp == equal_sum:
                cnt += 1
                i += 1
            elif tmp < equal_sum:
                i += 1
            else:
                tmp -= nums[i]
                i += 1

if if

# nums = [4, 3, 2, 3, 5, 2, 1]
# k = 4
nums = [10,10,10,7,7,7,7,7,7,6,6,6]
k = 3
print(Solution().canPartitionKSubsets(nums, k))