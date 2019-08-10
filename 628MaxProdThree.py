"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[0] * nums[1]* nums[-1], nums[-1] * nums[-2] * nums[-3])

    def maximumProduct2(self, nums):
        # keep track of 3 max and 2 min
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n

            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n

        return max(min1*min2*max1, max1*max2*max3) # the only solution candidate

# nums = [1,2,3]
nums = [-1,-2,-3]
print(Solution().maximumProduct2(nums))