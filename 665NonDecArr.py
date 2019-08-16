"""
Given an array with n integers, your task is to check if it could become non-decreasing
by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]: # look for target pair
                cnt += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]: # [20 30 25] modify middle
                    nums[i] = nums[i - 1]
                else: # [20 30 10] modify right
                    nums[i + 1] = nums[i]

            if cnt > 1:
                return False
        return True

    def checkPossibility2(self, nums):
        # greedy, find i with nums[i-1]>nums[i]
        # modify nums[i-1] or nums[i], e.g, [3,4,2,3]
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]: # find the wrong order pair
                cnt += 1
                if i < 2 or nums[i - 2] <= nums[i]: # decide which modify which one
                    nums[i - 1] = nums[i]  # modify nums[i-1]
                else:
                    nums[i] = nums[i - 1]  # modify nums[i]

        # By the end, array becomie non-decreasing array
        return cnt <= 1

    def checkPossibility3(self, nums):
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)

    def checkPossibility4(self, nums):
        p = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if p is not None:
                    return False
                p = i # look for target index

        """
        these are all conditions changing one val make non-decreasing array possible
        """
        return (p is None or p == 0 or p == len(nums) - 2 or
                nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2])




# nums = [4,2,3] #T
nums = [4,2,1] #F
# nums = [3,4,2,3] #F
# nums = [2,3,3,2,4] #T
print(Solution().checkPossibility(nums))