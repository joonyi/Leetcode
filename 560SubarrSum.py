"""
Given an array of integers and an integer k, you need to find the total number of
continuous subarrays whose sum equals to k.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # prefix sum
        import collections
        count = collections.Counter()
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)

        res = 0
        for n in prefix:
            res += count[n]
            count[n + k] += 1

        return res

    def subarraySum2(self, nums, k):
        import collections
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in nums:
            psum += i
            res += c[psum - k]
            c[psum] += 1
        return res

    def subarraySum3(self, nums, k):
        # Fastest
        count = 0
        sum = 0
        prefix = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in prefix:
                count += prefix[sum-k]

            prefix[sum] = prefix.get(sum , 0) + 1
        return count

# nums, k = [1,1,1], 2
nums, k = [3,4,7,2,-3,1,4,2], 7
print(Solution().subarraySum3(nums, k))