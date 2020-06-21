"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

1. Rank is an integer starting from 1.
2. The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
3. Rank should be as small as possible.

"""
from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = dict()
        rank = 1
        for e in sorted(set(arr)):
            ranks[e] = rank
            rank += 1

        return [ranks[e] for e in arr]


arr = [40, 10, 20, 30]
arr = [100,100,100]
arr = [37,12,28,9,100,56,80,5,12]
print(Solution().arrayRankTransform(arr))
