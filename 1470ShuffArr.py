"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].
"""

from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = [0] * (2*n)
        j = 0
        for i in range(n):
            res[j], res[j+1] = nums[i], nums[i+n]
            j += 2

        return res

nums = [2,5,1,3,4,7]
n = 3 # [2,3,5,4,1,7].
nums = [1,2,3,4,4,3,2,1]
n = 4 # [1,4,2,3,3,2,4,1]
nums = [1,1,2,2]
n = 2 # [1,2,1,2]
print(Solution().shuffle(nums, n))
