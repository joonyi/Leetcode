"""
We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j),
we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted
once in the final answer.)
"""
class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Brute Force TLE
        res = set()
        for i in range(len(A)):
            n = 0
            for j in range(i, len(A)):
                for a in A[i:j+1]:
                    n |= a
                res.add(n)

        return len(res)

    def subarrayBitwiseORs2(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur # union
        return len(ans)

A = [1,2,4]
print(Solution().subarrayBitwiseORs2(A))