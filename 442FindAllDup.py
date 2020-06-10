"""
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?
"""

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            nums[idx] = -nums[idx]
        return res

    def findDuplicates2(self, nums):
        dup = {}
        lis = []
        for num in nums:
            if num in dup:
                dup[num] += 1
                lis.append(num)
            else:
                dup[num] = 1

        return lis


nums = [4,3,2,7,8,2,3,1]
print(Solution().findDuplicates2(nums))
