"""
Given an integer array arr. You have to sort the integers in the array in ascending order
by the number of 1's in their binary representation and in case of two or more integers
have the same number of 1's you have to sort them in ascending order.

Return the sorted array.
"""


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(bin(max(arr))) - 2
        buckets = [[] for _ in range(n)]
        for a in arr:
            ones = bin(a).count('1')
            buckets[ones].append(a)

        res = []
        for bucket in buckets:
            if bucket:
                bucket.sort()
                res.extend(bucket)
        return res

    def sortByBits2(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


arr = [0,1,2,3,4,5,6,7,8]
arr = [1024,512,256,128,64,32,16,8,4,2,1]  # [1,2,4,8,16,32,64,128,256,512,1024]
print(Solution().sortByBits2(arr))