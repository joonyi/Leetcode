"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        size = 2**n
        subset = []
        powerset = []
        for i in range(size):
            for j in range(n):
                if i & (1 << j) != 0:
                    subset.append(nums[j])
            powerset.append(subset)
            subset = []

        return powerset

    def subsets2(self, nums):
        powerset = []
        subset = []

        def findSubset(nums, subset, i):
            if i == len(nums):
                powerset.append(subset[:])
            else:
                findSubset(nums, subset, i + 1)
                subset.append(nums[i])
                findSubset(nums, subset, i + 1)
                subset.pop()

        findSubset(nums, subset, 0)
        return powerset


nums = [1,2,3]
print(Solution().subsets(nums))