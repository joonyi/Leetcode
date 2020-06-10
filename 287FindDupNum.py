"""
Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive), prove that at least one duplicate number
must exist. Assume that there is only one duplicate number,
find the duplicate one.
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

        return -1

    def findDuplicate2(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return -1

    def findDuplicate3(self, nums):
        # Prove that at least on duplicate number
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find that number
        p1 = nums[0]
        p2 = tortoise
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1

nums  = [1,3,4,2,2]
print(Solution().findDuplicate3(nums))
