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
        res, dp = 0, 0
        prev = -1
        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res

    def numSubarrayBoundedMax2(self, A, L, R):
        # j start index of subarray
        # cnt length of subarray
        j = cnt = res = 0
        for i in range(len(A)):
            if A[i] >= L and A[i] <= R:
                res += i - j + 1
                cnt = i - j + 1
            elif A[i] < L:
                res += cnt
            else:
                j = i + 1
                cnt = 0
        return res

A, L, R = [2,1,4,3], 2, 3 # 3
# [2] => +1 number of subarrays with max within L and R
# [2,1] => +1

# A, L, R = [2,9,2,5,6], 2, 8 # 7
# [2] => +1 number of subarrays with max within L and R
# [2,5] => +2
# [2,5,6] => +3
print(Solution().numSubarrayBoundedMax2(A, L, R))
