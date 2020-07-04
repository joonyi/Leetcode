"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements
are subset of nums2. Find all the next greater numbers for nums1's elements in the
corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number
to its right in nums2. If it does not exist, output -1 for this number.
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums2:
            return None
        diff = [-1] * (max(nums2)+1) # index represents nums1, value represents nxt greater
        res = [-1] * len(nums1)
        stack = []  # invariant of next greater value to this current value
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:  # next greater entry exist
                diff[nums2[i]] = stack[-1]
            stack.append(nums2[i])

        for i, num in enumerate(nums1):
            res[i] = diff[num]

        return res

nums1 = [4,1,2]  # [-1,3,-1]
nums2 = [1,3,4,2]
# nums1 = [2,4]  # [3,-1]
# nums2 = [1,2,3,4]
print(Solution().nextGreaterElement(nums1, nums2))