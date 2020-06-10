"""
Given a non-empty array containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Get all the possible sums
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        a = sum(nums) / 2.
        return (sum(nums) / 2.) in possible_sums  # this is for python2.7


    def canPartition2(self, nums):
        sums = 0
        for num in nums:
            sums += num

        if (sums & 1) == 1:
            return False

        target = sums // 2

        # dp[i][j] means whether the specific sum j can be gotten from the first i numbers
        dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        # Base case: dp[0][0] is true; (zero number consists of sum 0 is true)
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            dp[i][0] = True  # always for sum 0


        # Transition function: For each number, if we don't pick it, dp[i][j] = dp[i-1][j],
        # which means if the first i-1 elements has made it to j, dp[i][j] would also make it to j
        # (we can just ignore nums[i]). If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]],
        # which represents that j is composed of the current value nums[i] and the remaining
        # composed of other previous numbers. Thus, the transition function is
        # dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target]


nums = [1, 5, 11, 5]  # True
# nums = [1,2,3,5]  # False
# nums = [2]
print(Solution().canPartition2(nums))
