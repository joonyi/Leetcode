"""
Given an integer array sorted in non-decreasing order, there is exactly one integer
in the array that occurs more than 25% of the time.

Return that integer.
"""

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = arr[0]
        cnt = 0
        for i in range(len(arr)):
            if arr[i] == n:
                cnt += 1
            else:
                n = arr[i]
                cnt = 1
            if cnt > len(arr) / 4:
                return n

    def findSpecialInteger2(self, arr):
        n = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + n]:
                return arr[i]


# Can try binary search, because array is sorted
arr = [1,2,2,6,6,6,6,7,10]
# arr = [1]
# arr = [1,2,3,3]
print(Solution().findSpecialInteger2(arr))