"""
We define a harmounious array as an array where the difference between its maximum value and
its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence
among all its possible subsequences.
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Fast
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        res = 0
        for k in d:
            if k+1 in d and d[k] + d[k+1] > res:
                 res = d[k] + d[k+1]
        return res

    def findLHS2(self, nums):
        # TLE
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        res = 0
        for k in d.keys():
            if k + 1 in d.keys() and d[k] + d[k + 1] > res:
                res = d[k] + d[k + 1]
        return res

# nums = [1,3,2,2,5,2,3,7] # 5
# nums = [1,2,3,4] # 2
# nums = [1,1,1,1] # 0
# nums = [0,3,1,3,3,3,0,1,0,2,0,3,1,3,-3,2,0,3,1,2,2,-3,2,2,3,3] # 15
nums = [2,2,2,2,2,2,2,3,1,0,0,0,3,1,-1,0,1,1,0,0,1,1,2,2,2,0,1,2,2,3,2]
print(Solution().findLHS(nums))