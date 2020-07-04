"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
"""

from typing import List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # TLE
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    for l in range(len(D)):
                        if A[i] + B[j] + C[k] + D[l] == 0:
                            res += 1

        return res

    def fourSumCount2(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        two_sums = dict()
        for a in A:
            for b in B:
                sums = a + b
                if sums in two_sums:
                    two_sums[sums] += 1
                else:
                    two_sums[sums] = 1

        cnt = 0
        for c in C:
            for d in D:
                target = 0 - c - d
                if target in two_sums:
                    cnt += two_sums[target]
        return cnt

    def fourSumCount3(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = sorted([a + b for a in A for b in B])
        n = sorted([c + d for c in C for d in D])
        mi, ni = 0, len(n) - 1
        cnt = 0
        while mi < len(m) and ni >= 0:
            while mi < len(m) and m[mi] + n[ni] < 0:
                mi += 1  # move to larger num
            if mi < len(m):  # mi cant go out of bound
                while ni >= 0 and m[mi] + n[ni] > 0:
                    ni -= 1  # move to smaller num
            if mi < len(m) and ni >= 0 and m[mi] + n[ni] == 0:
                cm ,cn = 1, 1
                while mi < len(m) - 1 and m[mi] == m[mi + 1]:
                    mi += 1
                    cm += 1
                while ni > 0 and n[ni] == n[ni - 1]:
                    ni -= 1
                    cn += 1
                cnt += cm * cn
                mi += 1
                ni -= 1
        return cnt


# A, B, C, D = [ 1, 2], [-2,-1], [-1, 2], [ 0, 2]  # 2
A, B, C, D = [0,1,-1], [-1,1,0], [0,0,1], [-1,1,1]  # 17
print(Solution().fourSumCount2(A, B, C, D))

