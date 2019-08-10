"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs
in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are
both numbers in the array and their absolute difference is k.
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # TLE. Can be improved with set(nums) like findPairs4
        nums.sort()
        res = set()
        for i in range(1, len(nums)):
            for j in range(i):
                if abs(nums[i] - nums[j]) == k:
                    res.add((nums[j], nums[i]))
        return res

    def findPairs2(self, nums, k):
        import collections
        res = 0
        c = collections.Counter(nums) # convert nums to hash table
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res

    def findPairs3(self, nums, k):
        if len(nums) < 2 or k < 0:
            return 0

        cnt = 0
        nums.sort()
        r = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: # eliminate duplicates
                continue
            r = max(r, i + 1)  # this line make sure r keep up with i as i will continue in above
            # r = i + 1 # also works, but slower
            while r < len(nums):
                if nums[r] - k == nums[i]:
                    cnt += 1
                    break
                elif nums[r] - k < nums[i]:
                    r += 1
                else:
                    break

        return cnt

    def findPairs4(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        s = set(nums) # eliminate duplicates
        if k < 0:
            return 0
        elif k == 0:
            for i in s:
                if nums.count(i) > 1: # Two or more same number result in diff zero
                    count += 1
            return count
        elif k > 0:
            for i in s:
                if i + k in s:
                    count += 1
        return count

nums, k = [3,1,4,1,5], 2
# nums, k = [1, 2, 3, 4, 5], 1
# nums, k = [1, 3, 1, 5, 4], 0
# nums, k = [1,1,1,2,1], 1
# nums, k = [1,3,1,5,4], 0
print(Solution().findPairs3(nums, k))
