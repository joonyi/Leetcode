"""
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if not row or row[0] > target:
                continue
            left, right = 0, len(row) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if target < row[mid]:
                    right = mid
                else:
                    left = mid

            if row[left] == target or row[right] == target:
                return True

        return False


"""
Compare to 74 Search2D, treating matrix as sorted array will not work
bcs last element of previous row might be larger than first element of the next row
"""
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5  # T
# target = 20 # F
matrix = [[1,4],
          [2,5]
          ]
target = 2  # T
print(Solution().searchMatrix(matrix, target))
