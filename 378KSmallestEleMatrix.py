"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

return 13
"""
import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            # n = sum(bisect.bisect_right(row, mid) for row in matrix)
            n = 0
            for row in matrix:
                for num in row:
                    if mid >= num:
                        n += 1

            if n < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def kthSmallest2(self, matrix, k): # Fail
        count = 0
        for row in matrix:
            for num in row:
                count += 1
                if count == k:
                    return num


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(Solution().kthSmallest2(matrix,k))