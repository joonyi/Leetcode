"""
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N
papers have at least h citations each, and the other N − h papers have no more than h citations each."
"""
from bisect import bisect_left
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = N = len(citations)
        citations.sort()
        while h:
            i = bisect_left(citations, h)
            if citations[i - 1] == h:
                i -= 1
            if N - i >= h:
                return h
            h -= 1
        return 0

    def hIndex2(self, citations):
        N = len(citations)
        buckets = [0 for _ in range(N + 1)]
        for h in citations:
            if h >= N:
                buckets[N] += 1
            else:
                buckets[h] += 1

        cnt = 0
        for i in reversed(range(len(buckets))):
            cnt += buckets[i]
            if cnt >= i:
                return i
        return 0


citations = [3,0,6,1,5]
print(Solution().hIndex2(citations))