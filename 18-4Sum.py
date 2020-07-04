"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums
such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 4sum = 2sum + 2sum
        import  collections
        nums.sort()
        d = collections.defaultdict(set)
        res = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j] # right two sum
                for half in d[target - sum]: # half is left two sum
                    res.add(tuple(list(half) + [nums[i], nums[j]]))
            for k in range(i):
                d[nums[i] + nums[k]].add((nums[k], nums[i]))
        return list(res)

    def fourSum2(self, nums, target):
        # Based on two sum
        def findNsum(nums, target, N, result, results):
            # bcs nums is sorted, so below are conditions of early termination
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:  # two pointers solve sorted 2-sum problem
                l, r = 0, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:  # recursively reduce N
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]): # skip first number or skip when this is a duplicate
                        findNsum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results

    def fourSum3(self, nums, target):
        # Based on three sum
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                threeResult = self.threeSum(nums[i + 1:], target - nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results

    def threeSum(self, nums, target):
        results = []
        # nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1

        return results


nums, target = [1, 0, -1, 0, -2, 2], 0
print(Solution().fourSum(nums, target))
