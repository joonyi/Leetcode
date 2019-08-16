"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error,
one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error.
Your task is to firstly find the number occurs twice and then find the number that is missing.
Return them in the form of an array.
"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = [0] * (len(nums) + 1)
        for num in nums:
            cnt[num] += 1
        res = [0,0]
        for i in range(1, len(cnt)):
            if cnt[i] == 2:
                res[0] = i
            elif cnt[i] == 0:
                res[1] = i
        return res

    def findErrorNums2(self, nums):
        dup = -1
        missing = -1
        for n in nums:
            if nums[abs(n) - 1] < 0:
                dup = abs(n)
            else:
                nums[abs(n) - 1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1
        return [dup, missing]




# nums = [1,2,2,4] # [2,3]
# nums = [1,1] # [1,2]
nums = [2,2]
print(Solution().findErrorNums2(nums))