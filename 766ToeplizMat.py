"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Compare to top left
        # Can change thinking to compare with right bottom, easier to write
        m, n = len(matrix), len(matrix[0])
        for i in range(m-1, -1, -1):
            for j in range(n):
                if i == 0:
                    continue
                if j == 0:
                    continue
                else:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True

    def isToeplitzMatrix2(self, matrix):
        return all(matrix[i][j] == matrix[i + 1][j + 1] for i in range(len(matrix) - 1) for j in range(len(matrix[0]) - 1))

# matrix = [
#   [1,2,3,4],
#   [5,1,2,3],
#   [9,5,1,2]
# ]
matrix = [
  [1,2],
  [2,2]
]
print(Solution().isToeplitzMatrix(matrix))