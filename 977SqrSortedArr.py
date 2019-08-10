"""
Given an array of integers A sorted in non-decreasing order,
return an array of the squares of each number, also in sorted non-decreasing order.
"""
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = [0] * len(A)
        for i in range(len(A)):
            B[i] = A[i]**2

        return sorted(B)

    def sortedSquares2(self, A):
        return sorted([i**2 for i in A])

# A = [-4,-1,0,3,10]
A = [-7,-3,2,3,11]
print(Solution().sortedSquares2(A))