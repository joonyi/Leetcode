"""
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
"""
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane algorithm
        if not nums: return 0
        maxv = minv = res = nums[0]
        for n in nums[1:]:
            tmp = maxv
            maxv = max(n, maxv * n, minv * n)
            minv = min(n, tmp * n, minv * n)
            res = max(res, maxv)
        return res

    def maxProduct2(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1

        return max(A + B)



# nums = [2,3,-2,4]
# nums = [-2, 0 ,-1]
# nums = [-2,3,-4]
nums = [-4,-3,-2]
# nums = [-3,0,1,-2]
print(Solution().maxProduct(nums))