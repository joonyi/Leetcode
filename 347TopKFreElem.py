"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in dict.items():
            bucket[val].append(key)

        ret = []
        for row in  reversed(bucket):
            if not row:
                continue
            else:
                for i in range(len(row)):
                    ret.append(row[i])
                    if len(ret) == k:
                        return ret

nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums,k))
