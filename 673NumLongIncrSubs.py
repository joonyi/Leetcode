"""
Given an unsorted array of integers, find the number of longest increasing subsequence.
"""

class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        res, max_len = 0, 0
        length = [0] * N  # the maximum length of LIS ending at nums[i]
        cnt = [0] * N  # the number of LIS ending at nums[i]
        for i in range(N):
            length[i] = cnt[i] = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    if length[i] == length[j] + 1:
                        cnt[i] += cnt[j]
                    elif length[i] < length[j] + 1:
                        length[i] = length[j] + 1
                        cnt[i] = cnt[j]

            if max_len == length[i]:
                res += cnt[i]
            elif max_len < length[i]:
                max_len = length[i]
                res = cnt[i]

        return res


# nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
nums = [1,1,2,2]
# nums =[1,2,4,3,5,4,7,2]

print(Solution().findNumberOfLIS(nums))

