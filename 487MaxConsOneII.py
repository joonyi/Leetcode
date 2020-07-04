"""
Given a binary array, find the maximum number of consecutive 1s in this array
if you can flip at most one 0
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        cnt = [0] * 2
        idx, _max = 0, 0
        zero = False
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt[idx] += 1
                _max = max(_max, cnt[0] + cnt[1])
            else:
                zero = True
                idx = idx ^ 1  # flip btw 0 and 1
                cnt[idx] = 0

        if zero == True:
            _max += 1
        return _max

    def findMaxConsecutiveOnes2(self, nums):
        res, cur, cnt = 0, 0, 0
        for i in range(len(nums)):
            cnt += 1
            if nums[i] == 0:
                cur = cnt
                cnt = 0
            res = max(res, cur + cnt)

        return res

nums = [1,0,1,1,0]  # 4
nums = [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1] # 9
nums = [1,0,1,1,0,1,1]  # 5
print(Solution().findMaxConsecutiveOnes2(nums))
