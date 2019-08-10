"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from
the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
import heapq
class Solution:
    def kSmallestPairs(self, nums1, nums2, k): # my own try, not working
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []
        if len(nums1) * len(nums2) <= k:
            return [[a,b] for a in nums1 for b in nums2]

        left = 0
        right = max(nums1)+max(nums2)
        while left < right:
            mid = left + (right - left)//2
            ret = []
            for i in range(len(nums1)):
                j = 0
                while j < len(nums2) and nums1[i] + nums2[j] <= mid:
                    ret.append([nums1[i],nums2[j]])

                    j += 1

            if len(ret) == k:
                return ret
            if len(ret) < k:
                left = mid + 1
            else:
                right = mid

        return ret

    def kSmallestPairs2(self, nums1, nums2, k):
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1-n2, [n1, n2]))
                else:
                    if heap and -heap[0][0] > n1 + n2:
                        heapq.heappop(heap) # pop the smallest item, heap[0], min heap
                        heapq.heappush(heap, (-n1-n2, [n1, n2]))
                    else:
                        break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]

    def kSmallestPairs3(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        if k > len(nums1) * len(nums2):
            k = len(nums1) * len(nums2)
        res = []
        secondIndex = [0] * len(nums1)
        index = 0
        minIndex = 0
        min = 0
        i = 0
        while k > 0:
            if secondIndex[index] >= len(nums2):
                index += 1
            minIndex = index
            min = nums1[index] + nums2[secondIndex[index]]
            i = index

            while i < len(secondIndex)-1 and secondIndex[i] != 0:
                i += 1
                if min > nums1[i] + nums2[secondIndex[i]]:
                    min = nums1[i] + nums2[secondIndex[i]]
                    minIndex = i
            res.append([nums1[minIndex],nums2[secondIndex[minIndex]]])
            secondIndex[minIndex] += 1
            k -= 1

        return res


# nums1 = [-10,-4,0,0,6]
# nums2 = [3,5,6,7,8,100]
# k = 10
nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(Solution().kSmallestPairs3(nums1,nums2,k))