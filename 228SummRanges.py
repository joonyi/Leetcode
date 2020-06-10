"""
Given a sorted integer array without duplicates, return the summary of its ranges.
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # Collect the ranges, then format and return them
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [[]]
            ranges[-1][1:] = [n]
        return ['->'.join(map(str, r)) for r in ranges]


    def summaryRanges2(self, nums):
        res = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start != nums[i]:  # this means i has moved
                res.append(str(start) + "->" + str(nums[i]))
            else:  # i has not moved, so range by itself
                res.append(str(start))

            i += 1

        return res


nums = [0,1,2,4,5,7]  # ["0->2","4->5","7"]
# nums = [0,2,3,4,6,8,9]  # ["0","2->4","6","8->9"]
print(Solution().summaryRanges2(nums))