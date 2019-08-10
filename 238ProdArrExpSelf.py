"""
Given an array nums of n integers where n > 1,  return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Brilliant solution
        p = 1
        n = len(nums)
        output = []
        for i in range(0, n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

# forward = [1,1,2,6]
# backward = [24,12,4,1]
# result = [24,12,8,6]
nums = [1,2,3,4]
# nums = [1,0]
print(Solution().productExceptSelf(nums))