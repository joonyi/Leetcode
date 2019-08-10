"""
Given a string S, check if the letters can be rearranged so that two characters that are
adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.
"""
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        A = []
        for c, x in sorted((S.count(x), x) for x in set(S)): # c is occurrence, x is character
            if c > (N + 1) // 2:
                return ""
            A.extend(c * x)
        ans = [None] * N
        ans[::2], ans[1::2] = A[N // 2:], A[:N // 2] # most common letters on even index
        return "".join(ans)

    def reorganizeString2(self, S):
        import heapq
        pq = [(-S.count(x), x) for x in set(S)] # store negative for max heap
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) // 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)

            ans.extend([ch1, ch2]) # so that no char adjacent
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1)) # reduce one count
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))
        # might have one element still on the heap, which must have count of one
        return "".join(ans) + (pq[0][1] if pq else '')



S = "aabb"
# S = "aaab"
print(Solution().reorganizeString2(S))