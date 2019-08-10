"""
Given two arrays, write a function to compute their intersection.
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        return list((d1 & d2).elements())

    def intersect2(self, nums1, nums2):
        d1 = {}
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        res = []
        for i in nums2:
            if i in d1 and d1[i] > 0:
                res.append(i)
                d1[i] -= 1
        return res

# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersect2(nums1, nums2))