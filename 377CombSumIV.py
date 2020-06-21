"""
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def Search(res, target):
            for i in range(len(nums)):
                if target - nums[i] == 0:
                    self.count += 1
                elif target - nums[i] > 0:
                    res.append(nums[i])
                    Search(res, target - nums[i])
                    res.pop()


        self.count = 0
        Search([], target)
        return self.count

    def combinationSum42(self, nums, target):
        # dp with each entry is the number of possible combinations that
        #  up to this index which represents target
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                if num == i:
                    combs[i] += 1
                if num < i:
                    combs[i] += combs[i - num]
        return combs[target]



nums, target = [1,2,3], 4
# nums, target = [4,2,1], 32
print(Solution().combinationSum42(nums, target))