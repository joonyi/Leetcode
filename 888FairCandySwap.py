"""
Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy
that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange,
they both have the same total amount of candy.  (The total amount of candy a person has is
the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange,
and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.
"""

from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        """TLE"""
        sumA = sum(A)
        sumB = sum(B)
        for a in A:
            for b in B:
                total_A = sumA - a + b
                total_B = sumB - b + a
                if total_A == total_B:
                    return [a, b]

    def fairCandySwap2(self, A, B):
        """
        If Alice gives candy x, and receives candy y,
        then Bob receives candy x and gives candy y. Then, we must have
        Sa - x + y = Sb - y + x, rearrange the equation
        y = x + (Sb - Sa) // 2
        For every x Alice has, check if Bob has y
        """
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            y = x + (Sb - Sa) // 2
            if y in setB:
                return [x, y]


A, B = [1,1], [2,2]
A, B = [1,2], [2,3]
A, B = [2], [1,3]
A, B = [1,2,5], [2,4]
print(Solution().fairCandySwap2(A, B))

