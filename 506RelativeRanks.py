"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores,
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".
"""
class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return nums
        sort = sorted(nums, reverse=True)
        d = {}
        for i in range(len(sort)):
            if i == 0:
                d[sort[i]] = "Gold Medal"
            elif i == 1:
                d[sort[i]] = "Silver Medal"
            elif i == 2:
                d[sort[i]] = "Bronze Medal"
            else:
                d[sort[i]] = str(i + 1)

        for i in range(len(nums)):
            nums[i] = d[nums[i]]

        return nums


# nums = [5,4,3,2,1]
# nums = [1]
nums = [10,3,8,9,4]
print(Solution().findRelativeRanks(nums))