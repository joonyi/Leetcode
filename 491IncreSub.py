"""
Given an integer array, your task is to find all the different possible increasing subsequences
of the given array, and the length of an increasing subsequence should be at least 2 .
"""


class Solution(object):
    def findSubsequences(self, nums):

        d = {i: [[nums[i]]] for i in range(len(nums))}
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for l in d[j]:
                        d[i].append(l + [nums[i]])

        s = set()
        res = []
        for i in range(len(nums)):
            for l in d[i]:
                if len(l) < 2: continue # result must len >= 2
                if tuple(l) in s: continue # Avoid duplicate
                s.add(tuple(l))
                res.append(l)
        return res

    def findSubsequences2(self, nums):
        def find(p, nums, one, res):
            if p == len(nums):
                if len(one) > 1:
                    res.add(tuple(one))
                return
            if not one or nums[p] >= one[-1]:
                one.append(nums[p])
                find(p+1, nums, one, res)
                one.pop()
            find(p+1, nums, one, res)

        res = set() # use set to eliminate duplicate
        one = []
        find(0, nums, one, res)
        return res

    def findSubsequences3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def find(nums, index, temp, res):
            if len(temp) >= 2:
                res.append(temp[:])
            used = {}
            for i in range(index, len(nums)):
                if len(temp) > 0 and temp[-1] > nums[i]: # skip decreasing subsequence
                    continue
                if nums[i] in used: # to avoid duplicate
                    continue

                used[nums[i]] = True
                temp.append(nums[i])
                find(nums, i + 1, temp, res)
                temp.pop()

        res = []
        find(nums, 0, [], res)
        return res




nums = [4,6,7,7]
print(Solution().findSubsequences3(nums))