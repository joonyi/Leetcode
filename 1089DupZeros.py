"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the
remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.
"""
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1

        print(arr)

    def duplicateZeros2(self, arr):
        # Start from the back and adjust items to correct locations. If item is zero then duplicate it.
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0

        print(arr)


arr = [1,0,2,3,0,4,5,0]
# arr = [1,2,3]
Solution().duplicateZeros2(arr)