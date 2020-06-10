"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        mid = len(nums) // 2
        if len(nums) % 2 == 1:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid - 1]) / 2

    def findMedianSortedArrays2(self, nums1, nums2):
        N1 = len(nums1)
        N2 = len(nums2)
        if N1 < N2:
            return self.findMedianSortedArrays2(nums2, nums1) # make sure N2 is shorter
        lo, hi = 0, N2 * 2
        while lo <= hi:
            mid2 = (lo + hi) // 2 # Cut 2
            mid1 = N1 + N2 - mid2 # Cut 1
            L1 = float('-inf') if mid1 == 0 else nums1[(mid1-1) // 2]
            L2 = float('-inf') if mid2 == 0 else nums2[(mid2-1) // 2]
            R1 = float('inf') if mid1 == N1 * 2 else nums1[mid1 // 2]
            R2 = float('inf') if mid2 == N2 * 2 else nums2[mid2 // 2]

            if L1 > R2: # nums1 lower half is too big
                lo = mid2 + 1 # move towards right in nums1
            elif L2 > R1:
                hi = mid2 - 1 # move towards left in nums1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2 # found the right cut
        return -1



nums1, nums2 = [1, 3], [2]
# nums1, nums2 = [1,2], [3,4]
# nums1, nums2 = [], [1]
print(Solution().findMedianSortedArrays2(nums1, nums2))