"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row
and maximum in its column.
"""
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_set = set()
        max_set = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            x, y = i, 0
            _min = matrix[x][y]
            for j in range(1, n):
                if matrix[i][j] < _min:
                    _min = matrix[i][j]
                    x, y = i, j
            min_set.add((x,y))

        for j in range(n):
            x, y = 0, j
            _max = matrix[x][y]
            for i in range(1, m):
                if matrix[i][j] > _max:
                    _max = matrix[i][j]
                    x, y = i, j
            max_set.add((x, y))

        lucky = min_set & max_set
        res = []
        for i, j in lucky:
            res.append(matrix[i][j])
        return res

    def luckyNumbers2(self, matrix):
        mi = {min(row) for row in matrix}
        mx = {max(col) for col in zip(*matrix)}
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

    def luckyNumbers3(self, matrix):
        _min = [min(row) for row in matrix]
        _max = [max(col) for col in zip(*matrix)]
        res = []
        for i in _min:
            if i in _max:
                res.append(i)
        return res

matrix = [[3,7,8],[9,11,13],[15,16,17]]  # [15]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]  # [12]
# matrix = [[7,8],[1,2]]  # [7]

print(Solution().luckyNumbers3(matrix))