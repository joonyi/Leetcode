"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]
"""
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1

        return res + [lo]


# S = "IDID"
# S = "III"
S = "DDI"
print(Solution().diStringMatch(S))