"""
Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        size = 2 ** n
        powerset = []
        for i in range(size):
            subset = []
            for j in range(n):
                if i & (1 << j) != 0:
                    subset.append(nums[j])
            if subset not in powerset:
                powerset.append(subset)

        return powerset

    def subsetsWithDup2(self, nums):
        import collections
        res = [[]]
        for num, freq in collections.Counter(nums).items():
            res_len = len(res)
            for i in range(1, freq + 1):
                for r in res[:res_len]:
                    res.append(r + [num] * i)
        return res

    def subsetsWithDup3(self, nums):
        nums.sort()
        res = [[]]
        start = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                start = 0

            for j in range(start, len(res)):
                clone = res[start][:]
                clone.append(nums[i])
                res.append(clone)
                start += 1
        return res



nums = [1,2,2]
nums =[4,4,4,1,4] # [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]

print(Solution().subsetsWithDup3(nums))
