"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        basket = [0] * (len(nums) + 1)
        res = []
        for num in nums: # O(n)
            basket[num] += 1
        for i in range(1, len(basket)): # O(n)
            if basket[i] == 0:
                res.append(i)

        return res

    # Another idea, first iteration mark appeared numbers as negative, second iteration, find non-negative spot
    def findDisappearedNumbers2(self, nums):
        res = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)

        return res

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers2(nums))