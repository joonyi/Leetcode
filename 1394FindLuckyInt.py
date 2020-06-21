"""
Given an array of integers arr, a lucky integer is an integer which has a frequency in the array
equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers return the largest of them.
If there is no lucky integer return -1.
"""
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = dict()
        for a in arr:
            if a not in freq:
                freq[a] = 1
            else:
                freq[a] += 1

        res = -1
        for n in freq:
            if n == freq[n]:
                res = max(res, n)
        return res


arr = [2,2,3,4]
arr = [1,2,2,3,3,3]
arr = [2,2,2,3,3]
arr = [5]
print(Solution().findLucky(arr))
