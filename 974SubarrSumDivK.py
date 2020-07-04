"""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays
that have a sum divisible by K.
"""

from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # TLE
        n = len(A)
        cnt = 0
        for i in range(n):
            for j in range(i, n):
                sums = sum(A[i:j + 1])
                if sums % K == 0:
                    cnt += 1
        return cnt

    def subarraysDivByK2(self, A: List[int], K: int) -> int:
        # TLE
        n = len(A)
        cnt = 0
        sums = [[0] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if i == j:
                    sums[i][j] = A[i]
                else:
                    sums[i][j] = A[j] + sums[i][j-1]

                if sums[i][j] % K == 0:
                    cnt += 1

        return cnt

    def subarraysDivByK3(self, A: List[int], K: int) -> int:
        # Prefix sum: Let P[i+1] = A[0] + A[1] + ... + A[i]. Then each subarray can be
        # written as P[j] - P[i] for j > i
        import collections
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K) # prefix sum module K

        count = collections.Counter(P)
        """
        With P[1],P[2],P[3],P[5], combination 4 pick 2 = 6
        namely A[1:2], A[1:3], A[1:5], A[2:3], A[2:5], A[3:5]
        """
        sums = []
        for v in count.values():
            sums.append(v * (v - 1) // 2)  # combination v pick 2
        return sum(sums)

    def subarraysDivByK4(self, A, K):
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K  # store the remainder count
            # for any SUM[i] if its remainder is same as remainder of any other SUM[some index] then their sum % k == 0
            res += count[prefix]
            count[prefix] += 1
        return res


A, K = [4, 5, 0, -2, -3, 1], 5
print(Solution().subarraysDivByK4(A, K))
