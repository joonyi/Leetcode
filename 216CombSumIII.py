"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers
from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def search(n, path, start, res):
            if len(path) == k:
                if n == 0:
                    res.append(path)
                return

            for i in range(start, 10):
                search(n - i, path + [i], i + 1, res)

        res = []
        search(n, [], 1, res)
        return res

    def combinationSum2(self, k, n):
        from itertools import combinations
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]

k, n = 3, 9
print(Solution().combinationSum3(k, n))