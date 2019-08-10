"""
Length of Longest Fibonacci Subsequence
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
"""
from collections import defaultdict
class Solution(object):
    def lenLongestFibSubseq(self, A):
        index = {x: i for i, x in enumerate(A)}
        longest = defaultdict(lambda: 2) # [1,2] is fib sequence with length 2

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None) # compute prev fib, use minus, instead addition, to prevent overflow
                if i is not None and i < j: # i exist, connect to the previous node
                    longest[j, k] = longest[i, j] + 1
                    cand = longest[j, k]
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0



# A = [1,2,3,4,5,6,7,8]
A = [1,3,7,11,12,14,18]
print(Solution().lenLongestFibSubseq(A))