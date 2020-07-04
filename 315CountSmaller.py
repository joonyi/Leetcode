"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the
right of nums[i].
"""

from typing import List
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # TLE O(n^2)
        cnt = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    cnt[i] += 1

        return cnt

    def countSmaller2(self, nums: List[int]) -> List[int]:
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def countSmaller3(self, nums: List[int]) -> List[int]:
        cnt = [0] * len(nums)
        idx = [i for i in range(len(nums))]
        self.mergesort(nums, idx, cnt, 0, len(nums) - 1)
        return cnt

    def mergesort(self, nums, idx, cnt, start, end):
        if end <= start:
            return
        mid = (start + end) // 2
        self.mergesort(nums, idx, cnt, start ,mid)
        self.mergesort(nums, idx, cnt, mid + 1, end)
        self.merge(nums, idx, cnt, start ,end)

    def merge(self, nums, idx, cnt, start, end):
        mid = (start + end) // 2
        lefti = start
        righti = mid + 1
        rightCount = 0
        newi = [0] * (end - start + 1)

        sorti = 0
        while lefti <= mid and righti <= end:
            if nums[idx[righti]] < nums[idx[lefti]]:
                newi[sorti] = idx[righti]
                rightCount += 1
                righti += 1
            else:
                newi[sorti] = idx[lefti]
                cnt[idx[lefti]] += rightCount
                lefti += 1
            sorti += 1

        while lefti <= mid:
            newi[sorti] = idx[lefti]
            cnt[idx[lefti]] += rightCount
            lefti += 1
            sorti += 1

        while righti <= end:
            newi[sorti] = idx[righti]
            sorti += 1
            righti += 1

        for i in range(start, end + 1):
            idx[i] = newi[i - start]


# Other solutions: Segment Tree, Binary indexed tree, Binary search tree
# nums = [5,2,6,1]
# nums = [5,1,2,1]
nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
# [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
# nums = [0,2,1]  # [0,1,0]
print(Solution().countSmaller3(nums))
