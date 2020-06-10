"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its
upper left corner (row1, col1) and lower right corner (row2, col2).

Ex:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""

class NumMatrix(object):
    # Caching Square sum
    def __init__(self, matrix):
        if not matrix:
            return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.sum[i + 1][j + 1] = self.sum[i + 1][j] + self.sum[i][j + 1] + matrix[i][j] - self.sum[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.sum[row2 + 1][col2 + 1] - self.sum[row1][col2 + 1] - self.sum[row2 + 1][col1] + self.sum[row1][col1]


class NumMatrix2(object):
    # Caching rows
    def __init__(self, matrix):
        if not matrix: return
        n, m = len(matrix), len(matrix[0])
        self.sum = [[0 for _ in range(n + 1)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.sum[i][j + 1] = self.sum[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        accum = 0
        for i in range(row1, row2 + 1):
            accum += self.sum[i][col2 + 1] - self.sum[i][col1]
        return accum

matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]

obj = NumMatrix2(matrix)
print(obj.sumRegion(2,1,4,3)) # 8
print(obj.sumRegion(1,1,2,2)) # 11
print(obj.sumRegion(1,2,2,4)) # 12
print(obj.sumRegion(0,0,1,1)) # 14