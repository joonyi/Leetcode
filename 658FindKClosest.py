"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array.
The result should also be sorted in ascending order. If there is a tie, the smaller elements
are always preferred.
"""

from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid - 1

        i = left
        if i == 0:
            return arr[:k]
        elif i >= len(arr):
            return arr[-k:]
        else:
            if i - k < 0:
                return arr[:k]
            else:
                # The problem with this solution is that when x is not in arr
                # we don't know the left or right of i we get is closest to x
                return arr[i-k:i]

    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            """
            Assume arr[mid] to arr[mid + k] is sliding window. Search for the start of the window
            If x - A[mid] > A[mid + k] - x,
            it means A[mid + 1] ~ A[mid + k] is better than A[mid] ~ A[mid + k - 1],
            and we have mid smaller than the right i.
            So assign left = mid + 1
            """
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

    def findClosestElements3(self, arr: List[int], k: int, x: int) -> List[int]:
        # Two pointers start at two ends, look for both end of the window
        left, right = 0, len(arr) - 1
        while right - left >= k:
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1
        return arr[left: left + k]


# arr, k, x = [1,2,3,4,5], 4, 3  # [1,2,3,4]
# arr, k, x = [1,2,3,4,5], 4, -1  # [1,2,3,4]
# arr, k, x = [0,0,1,2,3,3,4,7,7,8], 3, 5  # [3,3,4]
arr, k, x = [1,1,1,10,10,10], 1, 9  # [10]
# arr, k, x = [1], 1, 1  # [1]
print(Solution().findClosestElements3(arr, k, x))
