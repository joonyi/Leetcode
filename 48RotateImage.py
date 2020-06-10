"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        clockwise rotate
        first reverse up to down, then swap the symmetry
        1 2 3     7 8 9     7 4 1
        4 5 6  => 4 5 6  => 8 5 2
        7 8 9     1 2 3     9 6 3
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)


    def rotate2(self, matrix):
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))] # list comprehension

        print(matrix)

    def rotate3(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            for j in range(n // 2):
                row[j], row[~j] = row[~j], row[j] # [~j] is [n-1-j], swap the first and last element

        print(matrix)


"""
 * anticlockwise rotate
 * first reverse left to right, then swap the symmetry
 * 1 2 3     3 2 1     3 6 9
 * 4 5 6  => 6 5 4  => 2 5 8
 * 7 8 9     9 8 7     1 4 7
"""
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
Solution().rotate3(matrix)