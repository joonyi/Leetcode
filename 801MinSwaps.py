"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the
same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
It is guaranteed that the given input always makes it possible.
"""

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # swap[n] means the minimum swaps to make the A[i] and B[i] strictly increasing
        # not_swap[n] is the same with A[n] and B[n] not swapped.
        N = len(A)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0], swap[0] = 0, 1
        for i in range(1, N):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                not_swap[i] = not_swap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                not_swap[i] = min(not_swap[i], swap[i - 1])
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
        return min(swap[-1], not_swap[-1])


    def minSwap2(self, A, B):
        swap = 1
        no_swap = 0
        for i in range(1, len(A)):
            if A[i - 1] >= B[i] or B[i - 1] >= A[i]:
                # In this case, the ith manipulation should be same as the i-1th manipulation
                swap += 1
            elif A[i - 1] >= A[i] or B[i - 1] >= B[i]:
                # In this case, the ith manipulation should be the opposite of the i-1th manipulation
                tmp = swap
                swap = no_swap + 1
                no_swap = tmp
            else:
                # Either swap or fix is OK. Let's keep the minimum one
                _min = min(swap, no_swap)
                swap = _min + 1
                no_swap = _min

        return min(swap, no_swap)


A = [1, 3, 5, 4]
B = [1, 2, 3, 7]

print(Solution().minSwap2(A, B))