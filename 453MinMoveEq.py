"""
Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is
incrementing n - 1 elements by 1.
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)

# sum of all the numbers, before any moves;
# minNum as the min number int the list
# n is the length of the list
# After, say m moves, we get all the numbers as x
# sum + m * (n - 1) = x * n and x = minNum + m
# bcs every move will add to minNum
# sum + m * (n - 1) = (minNum + m) * n => sum - minNum * n = m


nums = [1,2,3]
print(Solution().minMoves(nums))