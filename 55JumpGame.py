"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # TLE
        # Construct a reach list to record reachability of each element
        reach = [False] * len(nums)
        reach[0] = True
        for i in range(len(reach)):
            if reach[i] == True:
                for j in range(1, nums[i] + 1):
                    if i + j < len(reach):
                        reach[i + j] = True
                    elif i + j == len(reach) - 1:
                        return True

        return reach[-1]

    def canJump2(self, nums):
        # Calculate the max reach from each elements
        # If can reach final, return True
        i = 0
        reach = 0
        while i < len(nums) and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1
        return i == len(nums)

    def canJump3(self, nums):
        # Traverse start from backward
        # if goal changed from len to 0, return True
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return not goal


nums = [2,3,1,1,4]  # T
# nums = [0]  # T
# nums = [2,0]  # T
# nums = [3,2,1,0,4]  # F
# nums = [1,1,1,0]  # T
print(Solution().canJump3(nums))
