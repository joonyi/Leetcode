"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a
subsequence ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks
whether there is a 132 pattern in the list.

Note: n will be less than 15,000.
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Brute Force TLE
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[k] > nums[i] and nums[j] > nums[k]:
        #                 return True

        # Improve brute force by finding i, j pair first, then only find k
        min_i = float('inf')
        for j in range(len(nums)-1):
            min_i = min(min_i, nums[j])
            for k in range(j+1, len(nums)):
                if nums[k] < nums[j] and min_i < nums[k]:
                    return True

        return False

    def find132pattern2(self, nums):
        interval = []
        i = 1
        s = 0
        while i < len(nums):
            if nums[i] <= nums[i-1]:
                if s < i - 1:
                    interval.append([nums[s], nums[i-1]])
                s = i
            for a in interval:
                if nums[i] > a[0] and nums[i] < a[1]:
                    return True
            i += 1
        return False

    def find132pattern3(self, nums):
        s3 = float('inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while stack and nums[i] > stack[-1]:
                    s3 = stack[-1]
                    stack.pop()
            stack.append(nums[i])

# nums = [1,2,3,4] # False
# nums = [3,1,4,2] # True
# nums = [-1,3,2,0] #True
# nums = [1,0,1,-4,-3] # False
nums = [-2,1,2,-2,1,2] # True
print(Solution().find132pattern3(nums))