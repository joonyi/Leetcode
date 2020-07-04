"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""

from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = [float('inf')] * len(arr)
        min_abs = float('inf')
        for i in range(1, len(arr)):
            diff[i] = arr[i] - arr[i - 1]
            if min_abs > diff[i]:
                min_abs = diff[i]

        res = []
        for i in range(1, len(arr)):
            if diff[i] == min_abs:
                res.append([arr[i-1], arr[i]])

        return res

    def minimumAbsDifference2(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]


arr = [4,2,1,3]  # [[1,2],[2,3],[3,4]]
# arr = [1,3,6,10,15]  # [[1,3]]
# arr = [3,8,-10,23,19,-4,-14,27]  # [[-14,-10],[19,23],[23,27]]
print(Solution().minimumAbsDifference2(arr))

