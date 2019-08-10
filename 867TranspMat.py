"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.
"""
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(A[0])
        B = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == j:
                    B[i][j] = A[i][j]
                else:
                    B[i][j] = A[j][i]

        return B

    def transpose2(self, A):
        return zip(*A)


A = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(A))