"""
Let's call an array A a mountain if the following properties hold:

1. A.length >= 3
2. There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Linear scan
        for i in range(1, len(A)):
            if A[i-1] < A[i] and A[i] > A[i+1]:
                return i

    def peakIndexInMountainArray2(self, A):
        # Binary search
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo

A = [0,1,0]
A = [0,2,1,0]
print(Solution().peakIndexInMountainArray2(A))