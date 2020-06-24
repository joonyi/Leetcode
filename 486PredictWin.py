"""
Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed by
the player 2 and then player 1 and so on. Each time a player picks a number,
that number will not be available for the next player. This continues until all the
scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.
You can assume each player plays to maximize his score.
"""
from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def maxScore(nums, s, e):
            if s == e:
                return nums[s]
            first = nums[s] - maxScore(nums, s + 1, e)
            last = nums[e] - maxScore(nums, s, e - 1)
            return max(first, last)

        return maxScore(nums, 0, len(nums) - 1) >= 0

    def PredictTheWinner2(self, nums: List[int]) -> bool:
        def maxScore(nums, s, e):
            if s == e:
                return nums[s]
            if (s, e) in memo:
                return memo[(s, e)]

            head = nums[s] - maxScore(nums, s + 1, e)
            tail = nums[e] - maxScore(nums, s, e - 1)
            memo[(s, e)] = max(head, tail)
            return memo[(s, e)]

        # memo = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        memo = {}
        return maxScore(nums, 0, len(nums) - 1) >= 0

    def PredictTheWinner3(self, nums: List[int]) -> bool:
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        # s, e represents start and end index
        # entry represents max score in range [s, e]
        for s in range(len(nums) - 1, -1, -1):
            dp[s][s] = nums[s]
            for e in range(s + 1, len(nums)):
                head = nums[s] - dp[s + 1][e]
                tail = nums[e] - dp[s][e - 1]
                dp[s][e] = max(head, tail)
        return dp[0][len(nums) - 1] >= 0



nums = [1, 5, 8, 4]
print(Solution().PredictTheWinner2(nums))

