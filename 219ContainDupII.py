"""
Given an array of integers and an integer k, find out whether there are two distinct
indices i and j in the array such that nums[i] = nums[j] and the absolute difference
between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # TLE
        if k == 0: return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True

        return False

    def containsNearbyDuplicate2(self, nums, k):
        hasht = {}

        for i, num in enumerate(nums):
            if num not in hasht:
                hasht[num] = i
            else:
                if abs(hasht[num] - i) <= k:
                    return True
                hasht[num] = i

        return False

# nums, k = [1,2,3,1], 3 # T
nums, k = [1,0,1,1], 1 # T
# nums, k = [1,2,3,1,2,3], 2 # F
print(Solution().containsNearbyDuplicate2(nums, k))
