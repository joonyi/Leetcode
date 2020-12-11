"""
Given two arrays of integers nums and index. Your task is to create target array under
the following rules:

Initially target array is empty.

From left to right read nums[i] and index[i], insert at index index[i] the value nums[i]
in target array.

Repeat the previous step until there are no elements to read in nums and index.

Return the target array.

It is guaranteed that the insertion operations will be valid.

"""
from typing import List
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(index)):
            res.insert(index[i], nums[i])

        return res

    def createTargetArray2(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            if index[i] == len(target):
                target.append(nums[i])
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target


nums = [0,1,2,3,4]
index = [0,1,2,2,1] # [0,4,1,3,2]
nums = [4,2,4,3,2]
index = [0,0,1,3,1] # [2,2,4,4,3]
print(Solution().createTargetArray2(nums, index))
