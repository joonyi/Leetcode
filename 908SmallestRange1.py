"""
Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K,
and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.
"""


class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2 * K)

"""
So, this is only interesting when A contains multiple, different values.
In the case of the second example, array A: [0, 10], K=2, the approach would be: "narrow" A 
by moving 0 toward 10 by adding 2 to A[0] and move A[1] (10) toward 0 by adding -2 to it 
(aka, subtracting 2 from it). The result then is: [2,8] which has a range 
(difference from largest to smallest) of 6.
"""
A = [0, 10]
K = 2
print(Solution().smallestRangeI(A, K))