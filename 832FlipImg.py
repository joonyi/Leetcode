"""
Given a binary matrix A, we want to flip the image horizontally, then invert it,
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0, 1, 1] results in [1, 0, 0].
"""

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    B[i][n-1-j] = 1
                else:
                    B[i][n - 1 - j] = 0

        return B

    def flipAndInvertImage2(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1 ^ i for i in row[::-1]] for row in A]
        # for 0<=x<=1, 1-x just invert it

# Another idea, use two pointers, one at start, one at end

A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(Solution().flipAndInvertImage2(A))