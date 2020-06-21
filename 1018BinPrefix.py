"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i]
interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
"""

class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans = [False] * len(A)
        n = 0
        for i in range(len(A)):
            n = 2 * n + A[i]
            if n % 5 == 0:
                ans[i] = True

        return ans

A = [0, 1, 1] # TFF
A = [1,1,1]  # FFF
A = [0,1,1,1,1,1] # TFFFTF
A = [1,1,1,0,1]  # FFFFF
print(Solution().prefixesDivBy5(A))
