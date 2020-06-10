"""
Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.
"""
import collections, random
class Solution(object):
    def __init__(self, nums):
        self.indexes = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.indexes[num].append(i)

    def pick(self, target):
        return random.choice(self.indexes[target])

class Solution2(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        cnt = 0
        for i in range(len(self.nums)):
            if nums[i] != target:
                continue
            cnt += 1
            if res == None: # initialize res
                res = i
            else:
                if random.randint(0, cnt - 1) == 0:
                    res = i # update res randomly with decreasing probability (cnt increasing)

        return res

nums = [1,2,3,3,3]
obj = Solution2(nums)
print(obj.pick(3))
print(obj.pick(1))