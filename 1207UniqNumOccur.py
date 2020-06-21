"""
Given an array of integers arr, write a function that returns true if and only if
the number of occurrences of each value in the array is unique.
"""
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """"""
        occur = {}
        for a in arr:
            occur[a] = occur.get(a, 0) + 1

        occurrence = sorted(occur.values())
        for i in range(len(occurrence) - 1):
            if occurrence[i] == occurrence[i + 1]:
                return False
        return True

    def uniqueOccurrences2(self, arr: List[int]) -> bool:
        occur = {}
        for a in arr:
            occur[a] = occur.get(a, 0) + 1

        occurrence = occur.values()
        return len(occurrence) == len(set(occurrence))


arr = [1,2,2,1,1,3]  # T
# arr = [1,2]  # F
# arr = [-3,0,1,-3,1,1,1,-3,10,0]  # T
print(Solution().uniqueOccurrences2(arr))
