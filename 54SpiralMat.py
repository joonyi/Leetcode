"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        while 0 <= i < m and 0 <= j < n and matrix[i][j] != '-':
            self.Spiral(matrix, i, j, m-i, n-j, res)
            i += 1
            j += 1

        return res

    def Spiral(self, matrix, i, j, m, n, res):
        while j < n and matrix[i][j] != '-':
            res.append(matrix[i][j])
            matrix[i][j] = '-'
            j += 1
        j -= 1
        i += 1
        while i < m  and matrix[i][j] != '-':
            res.append(matrix[i][j])
            matrix[i][j] = '-'
            i += 1
        i -= 1
        j -= 1
        while j >= 0 and matrix[i][j] != '-':
            res.append(matrix[i][j])
            matrix[i][j] = '-'
            j -= 1
        i -= 1
        j += 1
        while i >= 0 and matrix[i][j] != '-':
            res.append(matrix[i][j])
            matrix[i][j] = '-'
            i -= 1

# matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]
# matrix = [[1],]
print(Solution().spiralOrder(matrix))

