"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area,
formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.
"""

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Say the side lengths of the triangle are a <= b <= c
        # The necessary and sufficient condition for these lengths to
        # form a triangle of non-zero area is a + b > c.
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]

        return 0

A = [2,1,2]  # 5
# A = [1,2,1]  # 0
A = [3,2,3,4]  # 10
# A = [3,6,2,3]  # 8
print(Solution().largestPerimeter(A))