"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also
in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
"""
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: d.get(i, 1000 + i)) # how to explain this

    def relativeSortArray2(self, arr1, arr2):
        import collections
        ans, cnt = [], collections.Counter(arr1)  # Count each number in arr1
        for i in arr2:
            if cnt[i]: ans.extend([i] * cnt.pop(i))  # Sort the common numbers in both arrays by the order of arr2.
        for i in range(1001):
            if cnt[i]: ans.extend([i] * cnt.pop(i))  # Sort the numbers only in arr1.
        return ans

    def relativeSortArray3(self, arr1, arr2):
        # Count sort
        cnt = [0] * 1001
        for n in arr1:
            cnt[n] += 1
        i = 0
        for n in arr2:
            while cnt[n] > 0:
                arr1[i] = n
                i += 1
                cnt[n] -= 1
        for n in range(len(cnt)):
            while cnt[n] > 0:
                arr1[i] = n
                i += 1
                cnt[n] -= 1
        return arr1


arr1, arr2 = [2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
print(Solution().relativeSortArray3(arr1, arr2))

