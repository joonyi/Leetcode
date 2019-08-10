"""
Given two arrays, write a function to compute their intersection.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        for num1 in nums1:
            for num2 in nums2:
                if num1 == num2:
                    res.add(num1)
                    break

        return list(res)


    def intersection2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

# use set operation in python, one-line solution.
# brute-force searching, search each element of the first list in the second list.
# use dict to record all nums appeared in the first list, and then check if there are nums in the second list have appeared in the map.
# sort the two list, and use two pointer to search in the lists to find common elements.

# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(Solution().intersection(nums1, nums2))