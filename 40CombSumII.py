"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # Slowest
        def Search(i, path, res):
            if sum(path) > target:
                return
            elif sum(path) == target:
                res.add(tuple(path))
                return

            for j in range(i, len(candidates)):
                path.append(candidates[j])
                Search(j + 1, path, res)
                path.pop()

        candidates.sort()
        res = set()
        path = []
        i = 0
        Search(i, path, res)
        return list(res)

    def combinationSum22(self, candidates, target):
        def Search(nums, start, path, res, target):
            if not target:
                res.append(path)
                return
            for i in range(start, len(nums)):
                # Very important here! We don't use `i > 0` because we always want
                # to count the first element in this recursive step even if it is the same
                # as one before. To avoid overcounting, we just ignore the duplicates
                # after the first element.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if nums[i] > target:
                    break
                Search(nums, i + 1, path + [nums[i]], res, target - nums[i])

        candidates.sort()
        res = []
        Search(candidates, 0, [], res, target)
        return res

    def combinationSum23(self, candidates, target):
        # Fastest
        candidates.sort()
        dp = [set() for i in range(target + 1)] # each entry is set of sum equal to target
        dp[0].add(())
        for num in candidates:
            for t in range(target, num - 1, -1):
                for prev in dp[t - num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])

candidates, target = [10,1,2,7,6,1,5], 8
candidates, target = [2,5,2,1,2], 5
# candidates, target = [4,4,2,1,4,2,2,1,3], 6
print(Solution().combinationSum22(candidates, target))