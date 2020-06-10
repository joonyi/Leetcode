"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements
is repeated N times.

Return the element repeated N times.
"""
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A) // 2
        d = {}
        for n in A:
            d[n] = d.get(n, 0) + 1

            if d[n] == N:
                return n

        return -1

    def repeatedNTimes2(self, A):
        """
        Because there are N+1 unique elements and one of these element repeated N times
        So any repeated elements is the answer.

        Because the repeated elements must repeat N times, in 2N array, so the repeat distance
        cannot be longer than 3
        """
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i + k]:
                    return A[i]

A = [1,2,3,3]
A = [2,1,2,5,3,2]
A = [5,1,5,2,5,3,5,4]
print(Solution().repeatedNTimes2(A))