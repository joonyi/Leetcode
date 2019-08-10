"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.
"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # TLE
        def find(nums, S, i, total):
            if i == len(nums):
                if total == S:
                    self.res += 1
                return

            find(nums, S, i + 1, total + nums[i])
            find(nums, S, i + 1, total - nums[i])

        self.res = 0
        find(nums, S, 0, 0)
        return self.res

    def findTargetSumWays2(self, nums, S):
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)

    def findTargetSumWays3(self, nums, S):
        from collections import defaultdict
        memo = {0: 1} # target : how many ways
        for x in nums:
            m = defaultdict(int)
            for s, n in memo.items():
                m[s + x] += n # if contain s+x, increment n
                m[s - x] += n
            memo = m
        return memo[S]

    def findTargetSumWays4(self, nums, S):
        total = sum(nums)
        if S > total or S < -total:
            return 0

        dp = [0] * (2*total + 1) # so that range from -5 to 5
        dp[total] = 1 # index is target, val is how many ways
        for i in range(len(nums)):
            next = [0] * (2*total + 1)
            for k in range(2*total + 1):
                if dp[k] != 0:
                    next[k + nums[i]] += dp[k]
                    next[k - nums[i]] += dp[k]

            dp = next
        return dp[total+S]

nums, S = [1,1,1,1,1], 3
# nums, S = [0,1], 1
print(Solution().findTargetSumWays4(nums, S))
