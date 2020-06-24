"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Brute force, TLE O(n^2)
        cnt = 0
        for i in range(len(nums)):
            zero_one = [0, 0]
            for num in nums[i:]:
                if num == 0:
                    zero_one[0] += 1
                else:
                    zero_one[1] += 1

                if zero_one[0] == zero_one[1]:
                    cnt = max(cnt, sum(zero_one))

        return cnt

    def findMaxLength2(self, nums: List[int]) -> int:
        # 2 times length so that start with zero go left, start with one go right
        arr = [-2] * (2 * len(nums) + 1)  # can start with other than -2 as long as smaller than -1
        arr[len(nums)] = -1
        maxlen, cnt = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1

            if arr[cnt + len(nums)] >= -1:
                maxlen = max(maxlen, i - arr[cnt + len(nums)])
            else:
                arr[cnt + len(nums)] = i

        return maxlen

    def findMaxLength3(self, nums: List[int]) -> int:
        d = {0:-1}  # key:val -> cnt : i, start with cnt zero, index -1, so first loop start with i = 0
        maxlen, cnt = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt -= 1

            if cnt in d:
                maxlen = max(maxlen, i - d[cnt])
            else:
                d[cnt] = i

        return maxlen


# nums = [0,1]  # 2
# nums = [0,1,0]  # 2
nums = [0,0,1,0,0,0,1,1]  # 6
# nums = [0,1,1]  # 2
# nums = [0,0,0,0,1,1]  # 4
nums = [1,0,1,0,1,0]
print(Solution().findMaxLength2(nums))
