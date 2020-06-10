"""
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the
maximum array element in that subarray is at least L and at most R.
"""
class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        if not A: return 0
        maxToLeft = [-1] * len(A)
        maxToRight = [-1] * len(A)
        maxToLeft[0] = A[0]
        maxToRight[-1] = A[-1]
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                maxToLeft[i] = A[i - 1]
            else:
                maxToLeft[i] = A[i]
        for i in range(len(A) - 2, -1, -1):
            if A[i] >= A[i + 1]:
                maxToRight[i] = A[i]
            else:
                maxToRight[i] = A[i + 1]

        return

A, L, R = [2,1,4,3], 2, 3
print(Solution().numSubarrayBoundedMax(A, L, R))
