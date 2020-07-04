"""
Given a binary array, find the maximum number of consecutive 1s in this array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_so_far = count_max = 0
        for num in nums:
            if num == 1:
                count_so_far += 1
            else:
                count_max = max(count_max, count_so_far)
                count_so_far = 0

        count_max = max(count_max, count_so_far)
        return count_max


nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))

