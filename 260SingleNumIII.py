"""
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that appear only once.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        single = 0
        for num in nums:
            single ^= num

        # any num & with its negative will get a single bit
        # use that bit to partition nums into two group
        # one group will have number 0 on that bit position, another will have 1
        partition = single & -single

        a, b = 0, 0
        for num in nums:
            if num & partition == 0:
                a ^= num
            else:
                b ^= num

        return [a,b]



A = [2,1,2,3,4,1]
print(Solution().singleNumber(A))