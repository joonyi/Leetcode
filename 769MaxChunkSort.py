"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the
array into some number of "chunks" (partitions), and individually sort each chunk.
After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?
"""
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        """
        original: 0, 2, 1, 4, 3, 5, 7, 6
        max_curr: 0, 2, 2, 4, 4, 5, 7, 7
        sorted:   0, 1, 2, 3, 4, 5, 6, 7
        when max_curr[i] == sorted[i], cnt += 1
        """
        if not arr:
            return 0
        max_curr = [None] * len(arr)
        max_curr[0] = arr[0]
        for i in range(1, len(arr)):
            max_curr[i] = max(max_curr[i - 1], arr[i])

        cnt = 0
        for i in range(len(arr)):
            if max_curr[i] == i:
                cnt += 1
        return cnt

    def maxChunksToSorted2(self, arr):
        # simplified
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans

arr = [4,3,2,1,0] # 1
arr = [1,0,2,3,4] # 4
arr = [0, 2, 1, 4, 3, 5, 7, 6] # 5
print(Solution().maxChunksToSorted(arr))