"""
In MATLAB, there is a very useful function called 'reshape',
which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive
integers r and c representing the row number and column number of the wanted reshaped matrix,
respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the
same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal,
output the new reshaped matrix; Otherwise, output the original matrix.
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m*n != r*c: return nums

        p, q = 0, 0
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = nums[p][q]
                q += 1
                if q == n:
                    p += 1
                    q = 0

        return res

    def matrixReshape2(self, nums, r, c):
        m, n = len(nums), len(nums[0])
        if r*c != m*n:
            return nums
        res = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r*c):
            res[i//c][i%c] = nums[i//n][i%n] # impressive solution
        return res

# A = [[1,2],[3,4]]
# r = 1
# c = 4
A = [[1,2],[3,4],[5,6]]
r = 6
c = 1
print(Solution().matrixReshape2(A, r, c))