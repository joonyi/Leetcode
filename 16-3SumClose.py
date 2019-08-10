"""
Given an array nums of n integers and an integer target, find three integers in nums
such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # TLE
        res = []
        diff = float('inf')
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if diff > abs(total - target):
                        diff = abs(total - target)
                        res = nums[i] + nums[j] + nums[k]

        return res

    def threeSumClosest2(self, nums, target):
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total

                if abs(total - target) < abs(res - target):
                    res = total

                if total < target:
                    j += 1
                elif total > target:
                    k -= 1

        return res


# nums = [-1, 2, 1, -4]
# target = 1
# nums = [1,1,-1,-1,3]
# target = 3
nums = [-3,-2,-5,3,-4]
target = -1
print(Solution().threeSumClosest2(nums, target))