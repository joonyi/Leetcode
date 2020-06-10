"""
Given an array of integers A and let n to be its length.
Assume Bk to be an array obtained by rotating the array A k positions clock-wise,
we define a "rotation function" F on A as follow:

F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].
Calculate the maximum value of F(0), F(1), ..., F(n-1).
Note:
n is guaranteed to be less than 105.
"""
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # TLE
        maxR = float('-inf')
        n = len(A)
        for i in range(n):
            B = A[i:n] + A[:i]
            res = 0
            for i, v in enumerate(B):
                res += i * v
            maxR = max(maxR, res)
        return maxR

    def maxRotateFunction2(self, A):
        if len(A) == 0: return 0
        sum = iteration = 0
        for i in range(len(A)):
            sum += A[i]
            iteration += (A[i] * i)
        maxR = iteration
        for j in range(1, len(A)):
            iteration = iteration - sum + A[j-1] * len(A)
            maxR = max(maxR, iteration)
        return maxR

    def maxRotateFunction3(self, A):
        allSum = F = 0
        for i in range(len(A)):
            F += i * A[i]
            allSum += A[i]
        maxR = F
        for i in range(len(A) - 1, -1, -1):
            F = F + allSum - len(A) * A[i]
            maxR = max(F, maxR)
        return maxR

"""
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]
F(k-1) = 0 * Bk-1[0] + 1 * Bk-1[1] + ... + (n-1) * Bk-1[n-1]
       = 0 * Bk[1] + 1 * Bk[2] + ... + (n-2) * Bk[n-1] + (n-1) * Bk[0]
then,
F(k) - F(k-1) = Bk[1] + Bk[2] + ... + Bk[n-1] + (1-n)Bk[0]
              = (Bk[0] + ... + Bk[n-1]) - nBk[0]
              = sum - nBk[0]
         F(k) = F(k-1) + sum - nBk[0]
         
What is Bk[0]?
k = 0; B[0] = A[0];
k = 1; B[0] = A[len-1];
k = 2; B[0] = A[len-2];
"""

A = [4,3,2,6]
# A = [-2147483648,-2147483648]
print(Solution().maxRotateFunction3(A))