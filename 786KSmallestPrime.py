"""
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list,
we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints,
where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]

Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
"""

# Memory limit exceeded
class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        frac = []
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                frac.append([A[i]/A[j],A[i],A[j]])

        frac.sort(key = lambda frac:frac[0])

        return frac[K-1][1:]

A = [1,7]
K = 1
print(Solution().kthSmallestPrimeFraction(A,K))